import os
import json
import requests

def embed_string(input):

    headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}
    embedding_endpoint = "https://api-inference.huggingface.co/pipeline/feature-extraction/BAAI/bge-small-en-v1.5"
    embedding_payload = {
        "inputs": input,
        "options": {
            "wait_for_model": True
        }
    }
    embedding_response = requests.post(embedding_endpoint, headers=headers, json=embedding_payload)
    embeddings = list(json.loads(embedding_response.text))
    return embeddings