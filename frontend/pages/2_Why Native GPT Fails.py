import streamlit as st
from PIL import Image

# Placeholder for image paths
image_paths = ["path_to_image1.jpg", "path_to_image2.jpg", "path_to_image3.jpg"]

st.title("Challenges of Traditional GPT in Structuring Unstructured Data")

st.markdown(
    """
    When enterprises seek to summarize unstructured data, they encounter the critical challenge of creating consistent data
    structures across various sources. These structures are crucial in production environments to enable downstream
    applications (ML/BI tools, Salesforce, Jira, etc.) to deliver reliable insights to users. However, traditional language
    models, like GPT, face significant hurdles in this endeavor, as outlined below:

    ### Incomplete Data Structures

    Utilizing basic prompts with context, such as email threads between a seller and buyer, occasionally results in
    incomplete data structures when processed by GPT. This issue becomes more pronounced in large production environments,
    as illustrated below. The desired output is a json with the following variables per line item: item number, description, quantity,
    unit price, discount, total price.
    
    Notice, when using GPT natively, the line items description cuts off before completion and there is no 
    quantity, price, discount, or total price variables listed.
    """
)

st.image("frontend/images/image1.png", use_column_width=True)

st.markdown(
    """
    ### Incorrect Output Formatting

    GPT may exhibit incorrect formatting of the JSON data structure and introduce 'explanations' not requested by the
    prompt. This introduces the risk of inconsistency and hallucination, making it challenging for developers to utilize
    the generated data without meticulous prompt engineering.
    """
)

st.image("frontend/images/image2.png", use_column_width=True)

st.markdown(
    """
    ### Accuracy Challenges

    Achieving accuracy in language models is a persistent challenge. Ensuring that prompts guide models to provide precise
    representations of unstructured data remains an ongoing struggle. The example below highlights a correct structure and
    format but reveals inaccuracies in the content, such as incorrect unit prices and discount rates. The correct unit price 
    is 100 and the correct discount is 25. However, GPT out-of-the-box (without RAG) failed to record these numbers accurately.
    """
)

st.image("frontend/images/image3.png", use_column_width=True)

st.markdown(
    """
    ### Token Limitation Issues

    Organizations grappling with diverse data sources often face challenges due to token limits when utilizing GPT. Not all
    contextual information is relevant, requiring reliable parsing and retrieval from a consistently updated knowledge base.
    This underscores the need for Retrieval-Augmented Generation (RAG) technology.
    """
)

st.image("frontend/images/image4.png", use_column_width=True)

