import streamlit as st
from query import Query
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

with st.sidebar:
    st.subheader("About the app")
    st.info("This application uses a large language model to generate answers based on [Insurify](https://insurify.com)'s articles.")
    st.write("\n\n")
    st.markdown("**Resources used**")
    st.markdown("* [Zephyr-7B-Alpha LLM for Text Generation](https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha)")
    st.markdown("* [FlagEmbedding for Embedding Articles and Question](https://huggingface.co/BAAI/bge-small-en-v1.5)")
    st.markdown("* [LlamaIndex for Retrieval and Querying](https://www.llamaindex.ai)")
    st.markdown("* [HuggingFace Inference API for Hosting Models](https://huggingface.co/docs/api-inference/index)")
    st.write("\n\n")
    st.divider()
    st.caption("Created by [Richy Chen](https://linkedin/com/in/richychen/) using [Streamlit](https://streamlit.io/)🎈.")