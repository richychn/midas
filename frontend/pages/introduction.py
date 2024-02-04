import streamlit as st

def introduction_page():
    st.title("Meet the Team - Introduction")

    st.write("""
        Welcome to our application! Let's get to know the amazing team behind the scenes.
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
