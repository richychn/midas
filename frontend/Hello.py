import streamlit as st
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title="Midas",
    page_icon="👋",
)

st.title("Midas: Order from Chaos")
    
st.markdown(
    """
    In the ever-evolving landscape of data, the significance of well-organized and structured data representation cannot be 
    overstated. While Large Language Models (LLMs) excel at handling unstructured data, the practicalities of interacting 
    with various applications and individuals highlight the pivotal role of structured data.

    Structured data is not merely a convenience; it is a necessity. Take for example scenarios such as API interactions 
    or legal documentation. APIs require specific variables to function correctly, and contracts demand precise information 
    in designated fields to ensure legal validity. These are just a few of many examples that highlight the importance of 
    structured data. 

    Recognizing this imperative for consistently structured data representation and acknowledging the challenges 
    associated with data summarization, our solution introduces a revolutionary approach.

    By integrating Retrieval-Augmented Generation (RAG) technology, reinforced by LlamaIndex, our project efficiently 
    addresses challenges associated with structuring unstructured data. Traditional LLMs, when utilized for this task, 
    often struggle to maintain uniformity, impeding a standardized interpretation of information. Unlike these 
    conventional approaches, our solution ensures consistent and accurate data structuring, facilitating seamless 
    integration with tech pipelines. Additionally, it adeptly navigates token limitations, addressing the difficulties 
    traditional LLMs encounter when handling large datasets. Our approach guarantees systematic structuring of extensive 
    information, ensuring precision and efficiency even in the face of data complexity and scale.
    """
)

st.title("Our Team")

st.write("""
    Before we dive into our demo, let's first get to know the amazing team behind the scenes.
""")

team_members = [
    {
        "name": "Kai Hayden",
        "image_path": "frontend/images/demo.jpg",
        "introduction": "Hi, I'm Engineer 1. I specialize in...",
    },
    {
        "name": "Richy Chen",
        "image_path": "frontend/images/demo.jpg",
        "introduction": "Hello, I'm Engineer 2. My expertise lies in...",
    },
    {
        "name": "Bharathrham Kodungudi",
        "image_path": "frontend/images/demo.jpg",
        "introduction": "Greetings! I'm Engineer 3. I'm passionate about...",
    },
    {
        "name": "Mehul Khetrapal",
        "image_path": "frontend/images/demo.jpg",
        "introduction": "Hey there, I'm Engineer 4. I specialize in...",
    },
    {
        "name": "Mohnish Shah",
        "image_path": "frontend/images/demo.jpg",
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