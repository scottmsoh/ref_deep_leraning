import streamlit as st

# Set page configuration
st.set_page_config(page_title="NLP Dashboard", layout="wide")

from qa import q_and_a_page 
from sa import sentiment_analysis_page  


if "page" not in st.session_state:
    st.session_state.page = "main"  


def main_page():
    
    st.title("NLP Dashboard")
    st.markdown("<p style='text-align: center;'>Welcome to the NLP Dashboard! Choose a feature below:</p>", unsafe_allow_html=True)

   
    st.markdown(
        """
        <style>
        .button-container {
            display: flex;
            justify-content: center;
            gap: 50px;
            margin-top: 50px;
        }
        .custom-button {
            background-color: #4CAF50;
            color: white;
            padding: 20px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 18px;
            margin: 10px 2px;
            cursor: pointer;
            border: none;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }
        .custom-button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Sentiment Analysis", key="sentiment_analysis_button"):
            st.session_state.page = "sentiment_analysis"
    with col2:
        if st.button("Q&A Chatbot", key="qa_chatbot_button"):
            st.session_state.page = "q_and_a"


if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "sentiment_analysis":
    sentiment_analysis_page()
elif st.session_state.page == "q_and_a":
    q_and_a_page()
