# problem.py

import streamlit as st

def main():
    st.title("Example Use Case: Sales Orders")

    # Image Placeholder 1: Illustration of Unstructured Data
    st.image("path_to_unstructured_data_image.jpg", caption="Unstructured Data", use_column_width=True)

    # Problem Description
    st.markdown(
        """
        **The Problem:**
        
        Processing lengthy unstructured data can be time-consuming and resource-intensive. Traditional methods often 
        face token limits, leading to incomplete analysis and increased computational costs. Our solution utilizes 
        RAG technology, specifically tailored for tasks like retrieval, ingestion, and chunking, to overcome these challenges.
        """
    )

    # Image Placeholder 2: Illustration of RAG Technology
    st.image("path_to_rag_technology_image.jpg", caption="RAG Technology", use_column_width=True)

    # Importance of RAG
    st.markdown(
        """
        **The Importance of RAG:**
        
        Our implementation relies on Retrieval-Augmented Generation (RAG) technology, playing a pivotal role in mitigating 
        computation costs and addressing token limit challenges associated with extensive unstructured datasets. An integral 
        component of this efficiency lies in the technique of "chunking." In the context of our solution, chunking involves 
        breaking down large chunks of unstructured data into smaller, more manageable sections. By doing so, we strategically 
        reduce the likelihood of encountering token limit problems during data processing. This not only optimizes computational 
        resources but also ensures a more accurate and streamlined interpretation of unstructured information.

        """
    )

    # Example Use Case
    st.markdown(
        """
        **Example Use Case: Converting Sales Communication into Final Orders**
        
        Consider the scenario of sales calls and email chains. Our project excels in transforming audio transcripts and email 
        communications into finalized sales orders with up-to-date details. This process is streamlined through the RAG-powered 
        LlamaIndex, allowing for seamless retrieval, ingestion, and structuring of relevant information.
        """
    )

    # Image Placeholder 3: Illustration of Sales Communication Processing
    st.image("path_to_sales_communication_image.jpg", caption="Sales Communication Processing", use_column_width=True)

    # Additional Use Cases
    st.markdown(
        """
        **Versatility of Our Solution:**
        
        The outlined use case is just one example of how our product can add considerable value. 
        Our RAG-based approach with LlamaIndex is adaptable to various domains, making it a versatile solution for 
        structuring unstructured data efficiently.
        """
    )

    # Image Placeholder 4: Generic Illustration of Versatility
    st.image("path_to_generic_versatility_image.jpg", caption="Versatility in Use Cases", use_column_width=True)

    # Conclusion
    st.markdown(
        """
        Our project's emphasis on RAG technology, combined with LlamaIndex capabilities, positions us as a game-changer 
        in the domain of unstructured data processing. By addressing the challenges associated with large-scale data, 
        we bring unparalleled value to users across different industries.
        """
    )

if __name__ == "__main__":
    main()
