import streamlit as st
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title("Welcome to Team Midas! 👋")

st.write("""
Welcome to our application! Let's get to know the amazing team behind the scenes.
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
    image = Image.open(member["image_path"])
    introduction = member["introduction"]

    # Display image and introduction
    st.image(image, caption=f"{member['name']}", use_column_width=True)
    st.write(introduction)