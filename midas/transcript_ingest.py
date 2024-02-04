from llama_index import SimpleDirectoryReader
from llama_index.schema import TextNode
from llama_index.text_splitter import SentenceSplitter
from llama_index.vector_stores import AstraDBVectorStore
from datetime import datetime
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class TranscriptIngest:
    def __init__(self, file_path, namespace="transcripts", convo_id=1):
        self.file_path = file_path
        self.vector_store = AstraDBVectorStore(
            token=os.getenv('ASTRA_DB_APPLICATION_TOKEN'),
            api_endpoint=os.getenv('ASTRA_DB_API_ENDPOINT'),
            collection_name="midas_collection",
            embedding_dimension=384,
            namespace=namespace
        )
        
        self.documents = None
        self.text_with_metadata = None
        self.nodes = []

    def get_documents(self):
        self.documents = SimpleDirectoryReader(self.file_path).load_data()

    def get_text_with_metadata(self):
        text_data = []
        metadata = []
        for doc in self.documents:
            text_data.append(doc.text)
            title_split = doc.metadata['file_name'].split('__')
            conversation_id = title_split[0]
            date_list = title_split[1].split('.')[0]
            datetime_object = datetime.strptime(date_list, "%Y_%m_%d_%I_%M_%p")
            date_string = datetime_object.strftime("%m/%d/%Y, %H:%M")
            metadata.append({'convo_id': conversation_id, 'date': date_string})

        self.text_with_metadata = [(text, meta) for text, meta in zip(text_data, metadata)]

    def get_nodes(self):
        text_splitter = SentenceSplitter()
        text_chunks = []
        doc_idxs = []
        chunk_ids = []
        for doc_idx, doc in enumerate(self.text_with_metadata):
            cur_text_chunks = text_splitter.split_text(doc[0])
            text_chunks.extend(cur_text_chunks)
            doc_idxs.extend([doc_idx] * len(cur_text_chunks))
            chunk_ids.extend(list(range(len(cur_text_chunks))))
        
        for idx, text_chunk in enumerate(text_chunks):
            node = TextNode(
                text=text_chunk,
            )
            src_doc = self.text_with_metadata[doc_idxs[idx]]
            chunk_id = chunk_ids[idx]
            metadata = src_doc[1]
            metadata['chunk_id'] = chunk_id
            node.metadata = metadata
            self.nodes.append(node)

    def add_embeddings_to_nodes(self):
        upload_text = [i.text for i in self.nodes]

        headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"}
        embedding_endpoint = "https://api-inference.huggingface.co/pipeline/feature-extraction/BAAI/bge-small-en-v1.5"
        embedding_payload = {
                "inputs": upload_text,
                "options": {
                "wait_for_model": True
                }
            }
        embedding_response = requests.post(embedding_endpoint, headers=headers, json=embedding_payload)
        embeddings = list(json.loads(embedding_response.text))

        for node, embedding in zip(self.nodes, embeddings):
            node.embedding = embedding
    
    def upload_nodes(self):
        self.vector_store.add(self.nodes)

    def run(self):
        self.get_documents()
        self.get_text_with_metadata()
        self.get_nodes()
        self.add_embeddings_to_nodes()
        self.upload_nodes()