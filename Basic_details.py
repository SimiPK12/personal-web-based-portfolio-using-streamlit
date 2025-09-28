import streamlit as st
from PIL import Image
import os

# --- Page Config ---
st.set_page_config(page_title="Bhagya Bhagavath S Portfolio", layout="wide")

# --- Welcome Section ---
st.title("👋 Welcome to my Portfolio!")
st.header("Hi! I am Bhagya Bhagavath S")
st.subheader("Data Science student and aspiring ML Engineer 💻")

# --- Profile Section ---
col1, col2 = st.columns([1, 2])

with col1:
    IMG_PATH = os.path.join("Resources", "Images", "profile.jpg")
    if os.path.exists(IMG_PATH):
        image = Image.open(IMG_PATH)
        st.image(image, use_container_width=True)
    else:
        st.warning("Profile image not found. Please check path: resources/images/profile.jpg")

with col2:
    st.header("👤 Personal Details")
    st.write("""
    - **Name:** Bhagya Bhagavath S  
    - **Email:** bhagyabhagavath12@gmail.com  
    """)
    
    st.header("🎓 Education")
    st.write("""
    - **B.E. (Pursuing):** Atria Institute of Technology, Data Science Branch, Bangalore  
    - **PU (2023):** Mount Carmel PU College, PCMC Branch — **90%**  
    - **Schooling (2021):** Florence Public School — **93%**  
    """)
    
    st.header("🔗 Connect with Me")
    linkedin_url = "https://www.linkedin.com/in/bhagya-bhagavath-s-34ab31364/"  # replace with your LinkedIn
    github_url = "https://github.com/SimiPK12"          # replace with your GitHub
    
    st.write(f"[🌐 LinkedIn]({linkedin_url}) | [🐙 GitHub]({github_url})")

    st.header("💡 Skills")
    skills = ["Python", "Machine Learning", "Data Analysis", "EDA", "MySQL", "Rasa Chatbot", "Streamlit", "Data Visualization"]
    st.write(", ".join(skills))

# --- Highlights Section ---
st.header("🌟 Projects")
st.write("""
- **Healthcare Insurance EDA** – Exploratory Data Analysis project  
- **Rasa Chatbot** – Built a chatbot using Machine Learning  
- **Library Management System** – Implemented using MySQL  
- **Diamond Price Prediction** – Machine Learning model for regression  
- **Web-based Portfolio** – Created using Streamlit  
""")
