import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Set Streamlit page configuration for a futuristic design
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Set a futuristic color scheme
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121212;  /* Deep dark background */
        color: #EAEAEA;  /* Light text color */
    }
    .stButton>button {
        background-color: #6200EE;  /* Vibrant futuristic purple button */
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stTextInput>div>input {
        background-color: #1F1F1F;  /* Dark input field */
        color: #EAEAEA;  /* Light text inside input field */
        border: 1px solid #333333;  /* Subtle border */
        border-radius: 8px;
    }
    .stChatMessage {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title and logo
st.title("🤖 Gemini Pro - AI Chatbot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro anything...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
