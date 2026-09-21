from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

# Input api_key in the sidebar
with st.sidebar:
    strGPT_API_Key = os.getenv('OPENAI_API_KEY') 
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

# Initialize "messages" in st.session_state if not present
if "messages" not in st.session_state:
    st.session_state["messages"] = [
             {"role": "assistant", "content": "How can I help you?"}
        ]

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input, add it to the conversation history, and generate AI response
if prompt := st.chat_input():
    if not strGPT_API_Key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=strGPT_API_Key)
    st.session_state.messages.append({"role": "user", "content": prompt}) 
    st.chat_message("user").write(prompt) 
    response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages) 
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg}) 
    st.chat_message("assistant").write(msg)

