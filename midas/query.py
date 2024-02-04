from llama_index.vector_stores import VectorStoreQuery, AstraDBVectorStore
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class Query:
    def __init__(self, query_str=None, query_embedding=None, query_mode="default", top_k=4, namespace="sales"):
        self.query_str = query_str
        self.query_embedding = query_embedding
        self.query_mode = query_mode
        self.top_k = top_k
        self.namespace = namespace

    def embed_query(self):
        headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_TOKEN')}"}
        embedding_endpoint = "https://api-inference.huggingface.co/pipeline/feature-extraction/BAAI/bge-small-en-v1.5"
        embedding_payload = {
            "inputs": [self.query_str],
            "options": {
                "wait_for_model": True
            }
        }
        embedding_response = requests.post(embedding_endpoint, headers=headers, json=embedding_payload).text[0]
        self.query_embedding = list(json.loads(embedding_response.text))[0]

    def get_similar_nodes(self):
        vector_store_query = VectorStoreQuery(
            query_embedding=self.query_embedding, similarity_top_k=self.top_k, mode=self.query_mode
        )
        vector_store = AstraDBVectorStore(
            token=os.getenv('ASTRA_DB_APPLICATION_TOKEN'),
            api_endpoint=os.getenv('ASTRA_DB_API_ENDPOINT'),
            collection_name="midas_collection",
            embedding_dimension=384,
            namespace=self.namespace
        )
        query_result = vector_store.query(vector_store_query)
        return query_result.nodes
    
    def run(self):
        if self.query_embedding is None:
            self.embed_query()
        return self.get_similar_nodes()