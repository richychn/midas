import streamlit as st

def introduction_page():
        # Introduction
    st.title("LlamaLogic: Order from Chaos")
    
    st.markdown(
        """
        In today's data-centric environment, the need for well-organized, structured data representation is 
        pervasive across various individuals and organizations. Summarizing extensive data sources in a specified 
        structured manner presents a significant challenge. Traditional Large Language Models (LLMs) often 
        face difficulties in maintaining uniformity when organizing unstructured data consistently. This 
        inconsistency becomes a barrier to achieving a standardized and precise interpretation of information. 
        Recognizing the widespread demand for consistently structured data representation and the challenges 
        associated with data summarization, our solution introduces a groundbreaking approach.

        By incorporating Retrieval-Augmented Generation (RAG) technology, amplified by LlamaIndex, our project 
        provides an efficient and reliable solution to the challenges posed by unstructured data. It not only 
        ensures the consistent structuring of extensive information but also adeptly navigates the limitations 
        imposed by token constraints. This unique capability empowers our solution to deliver a precise, 
        structured interpretation of data consistently, even when dealing with massive datasets!
        """
    )
    

    st.write("""
        Before we dive into our demo, let's first get to know the amazing team behind the scenes.
    """)

    team_members = [
        {
            "name": "Kai Hayden",
            "image_path": "/Users/shahmohnish/Documents/midas/frontend/images/demo.jpg",
            "introduction": "Hi, I'm Engineer 1. I specialize in...",
        },
        {
            "name": "Richy Chen",
            "image_path": "/Users/shahmohnish/Documents/midas/frontend/images/demo.jpg",
            "introduction": "Hello, I'm Engineer 2. My expertise lies in...",
        },
        {
            "name": "Bharathrham Kodungudi",
            "image_path": "/Users/shahmohnish/Documents/midas/frontend/images/demo.jpg",
            "introduction": "Greetings! I'm Engineer 3. I'm passionate about...",
        },
        {
            "name": "Mehul Khetrapal",
            "image_path": "/Users/shahmohnish/Documents/midas/frontend/images/demo.jpg",
            "introduction": "Hey there, I'm Engineer 4. I specialize in...",
        },
        {
            "name": "Mohnish Shah",
            "image_path": "/Users/shahmohnish/Documents/midas/frontend/images/demo.jpg",
            "introduction": "Hi, I'm Engineer 5. My focus is on...",
        },
    ]

    # Display introductions for each team member
    for member in team_members:
        st.write(f"## {member['name']}")
        image = member["image_path"]
        introduction = member["introduction"]

        # Display image and introduction
        st.image(image, caption=f"{member['name']}", use_column_width=True)
        st.write(introduction)

if __name__ == "__main__":
    introduction_page()
