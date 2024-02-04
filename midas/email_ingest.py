from llama_parse import LlamaParse
from llama_index.text_splitter import SentenceSplitter
from llama_index.schema import TextNode
from llama_index.vector_stores import AstraDBVectorStore
import re 
import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

from midas.embeddings import embed_string

load_dotenv()


class EmailIngest:
    def __init__(self, file_path, namespace="sales", convo_id=0):
        self.file_path = file_path
        self.parser = LlamaParse(result_type="markdown")
        self.file_extractor = {".pdf": self.parser}
        self.text_splitter = SentenceSplitter()
        self.namespace = namespace

        self.document = None
        self.emails_with_metadata = []
        self.nodes = []
        self.convo_id = convo_id

        self.vector_store = AstraDBVectorStore(
            token=os.getenv('ASTRA_DB_APPLICATION_TOKEN'),
            api_endpoint=os.getenv('ASTRA_DB_API_ENDPOINT'),
            collection_name="midas_collection",
            embedding_dimension=384,
            namespace=self.namespace
        )

    def get_documents(self):
        self.document = LlamaParse(result_type="markdown").load_data(self.file_path)[0]

    def get_emails_with_metadata(self):
        emails = re.split("<.*@.*>\n*.*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)+ (?:0?[1-9]|[1-3][0-9]), [12][0-9]{3} at (?:[0-1]?[0-9]|2[0-3]):(?:[0-5][0-9]+) (?:AM|PM)\n*.*<.*@.*>", self.document.text)[1:]
        headers = re.findall("(<.*@.*>)\n*.*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)+ (0?[1-9]|[1-3][0-9]), ([12][0-9]{3}) at ([0-1]?[0-9]|2[0-3]):([0-5][0-9]+) (AM|PM)\n*.*(<.*@.*>)", self.document.text)

        for email, header in zip(emails, headers):
            sender = header[0]
            receiver = header[7]
            date = datetime.strptime(f'{header[1]} {header[2]}, {header[3]} {header[4]}:{header[5]} {header[6]}', '%b %d, %Y %I:%M %p')
            self.emails_with_metadata.append((email, {"sender": sender, "receiver": receiver, "date": date.strftime("%m/%d/%Y, %H:%M"), "convo_id": self.convo_id}))

    def get_nodes(self):
        text_chunks = []
        doc_idxs = []
        for doc_idx, doc in enumerate(self.emails_with_metadata):
            cur_text_chunks = self.text_splitter.split_text(doc[0])
            text_chunks.extend(cur_text_chunks)
            doc_idxs.extend([doc_idx] * len(cur_text_chunks))

        for idx, text_chunk in enumerate(text_chunks):
            node = TextNode(
                text=text_chunk,
            )
            src_doc = self.emails_with_metadata[doc_idxs[idx]]
            node.metadata = src_doc[1]
            self.nodes.append(node)

    def add_embeddings_to_nodes(self):
        upload_text = [i.text for i in self.nodes]

        embeddings = [embed_string(i) for i in upload_text]
    
        for node, embedding in zip(self.nodes, embeddings):
            node.embedding = embedding
    
    def upload_nodes(self):
        self.vector_store.add(self.nodes)

    def run(self):
        self.get_documents()
        self.get_emails_with_metadata()
        self.get_nodes()
        self.add_embeddings_to_nodes()
        self.upload_nodes()