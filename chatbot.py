import streamlit as st
import requests
import json

# Configure the page
st.set_page_config(
    page_title="Nexa Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title and description
st.title("Nexa AI")
st.markdown("""
This chatbot uses the DeepSeek-R1:1.5b model through Ollama.
Make sure you have Ollama running locally with the DeepSeek model installed.
""")

# Function to get response from Ollama
def get_ollama_response(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Error: {str(e)}"

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ollama_response(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.markdown("""
    This chatbot uses:
    - Streamlit for the web interface
    - Ollama for running the DeepSeek-R1:1.5b model locally
    - DeepSeek-R1:1.5b for generating responses
    """)
    
    st.header("Instructions")
    st.markdown("""
    1. Make sure Ollama is running locally
    2. Ensure the DeepSeek model is installed
    3. Type your message and press Enter
    4. Wait for the response
    """)
    
    # Clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun() 
