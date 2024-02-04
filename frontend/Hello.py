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
    Before we dive into a sample use case, let's first get to know the amazing team behind the scenes.
""")

team_members = [
    {
        "name": "Kai Hayden",
        "image_path": "frontend/images/Kai.png",
        "introduction": "Kai Hayden is a data scientist at Tesla, specializing in supply chain management. Armed with a Master's degree in Data Science from the University of Chicago, he is dedicated to pioneering the development of the world's premier vertically integrated logistics planning system.",
    },
        {
        "name": "Mehul Khetrapal",
        "image_path": "frontend/images/Mehul.png",
        "introduction": "Mehul Khetrapal is an AI Engineer at IBM, bringing expertise in AI governance within the financial services sector. Holding a Master's degree in Biomedical Engineering from the University of Southern California, Mehul is dedicated to pioneering responsible and ethical AI practices.",
    },
    {
        "name": "Bharath Kodungudi",
        "image_path": "frontend/images/Bharath.png",
        "introduction": "Bharath Kodungudi is a Data Analyst at BILL, where he collaborates with executive leadership to craft company and product strategy. Equipped with a Master's degree in Analytics (Data Science) from the Georgia Institute of Technology, Bharath integrates business and analytics to drive strategy.",
    },
        {
        "name": "Richy Chen",
        "image_path": "frontend/images/Richy.png",
        "introduction": "Richy Chen is a Product Manager at Insurify, where he is spearheading Real Time Bidding (RTB) API and B2B2C products, including innovative solutions like agency referrals. Richy holds a Bachelor's degree in Computer Science from the Claremont McKenna College.",
    },
    {
        "name": "Mohnish Shah",
        "image_path": "frontend/images/Mo.png",
        "introduction": "Mohnish Shah is a Product Manager at BILL focusing on automating the entire financial back office for SMBs. With a Master's in Analytics (Data Science) from the Georgia Institute of Technology, Mohnish aims to bring financial peace of mind by streamlining personal and corporate finances.",
    },
]

# Display introductions for each team member in two rows
col1, col2 = st.columns(2)

for i, member in enumerate(team_members):
    col = col1 if i < 3 else col2  # First row in col1, second row in col2
    with col:
        st.write(f"## {member['name']}")
        image = member["image_path"]
        introduction = member["introduction"]

        # Display image and introduction
        st.image(image, caption=f"{member['name']}", use_column_width=True)
        st.write(introduction)