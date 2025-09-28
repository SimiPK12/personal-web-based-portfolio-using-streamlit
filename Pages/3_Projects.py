import streamlit as st

# --- Projects Section ---
st.markdown("---")
st.subheader("💻 Projects")

# --- Healthcare Insurance EDA ---
with st.expander("📊 EDA Project - Health Care Insurance"):
    st.write("""
    - Cleaned and preprocessed raw data.  
    - Identified patterns, trends, and anomalies.  
    - Visualized distributions and correlations for insights.  
    """)

# --- Rasa Chatbot ---
with st.expander("🤖 ML Project - Rasa Chatbot"):
    st.write("""
    - Designed conversational flows and intents.  
    - Implemented NLP techniques for intent classification.  
    - Built a functional chatbot that can handle user queries.  
    """)

# --- Library Management (MySQL) ---
with st.expander("📚 Database Project - Library Management (MySQL)"):
    st.write("""
    - Designed normalized database schema with multiple tables.  
    - Implemented CRUD operations for books, students, and borrowing records.  
    - Ensured data integrity with primary and foreign keys.  
    """)

# --- Diamond Price Prediction ---
with st.expander("💎 ML Project - Diamond Price Prediction"):
    st.write("""
    - Conducted feature engineering and data preprocessing.  
    - Applied regression algorithms to predict diamond prices.  
    - Evaluated model performance using error metrics.  
    """)

# --- Web Portfolio ---
with st.expander("🌐 Web Project - Portfolio using Streamlit"):
    st.write("""
    - Designed interactive pages to showcase personal profile, education, and projects.  
    - Integrated images, markdown, and dynamic widgets.  
    - Deployed the portfolio for public access.  
    """)
