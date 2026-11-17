import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

from langchain_openai import ChatOpenAI  # LangChain Chatbot class using OpenAI models
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

# Input api_key in the sidebar
with st.sidebar:
    strOpenAI_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strOpenAI_API_Key)

LLM = ChatOpenAI(model="gpt-4o-mini")   # Initialize LangChain Chatbot model

# Function to get session history
def get_ai_response(messages):
    response = LLM.stream(messages)
    
    for chunk in response:
        yield chunk

st.title("💬 Langchain Chatbot ")        # Streamlit UI
st.caption("🚀 A Streamlit Chatbot powered by OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage("너는 사용자의 질문에 친절이 답하는 AI 챗봇이다."),
        AIMessage("How can I help you?")
    ]

# Display messages on the Streamlit screen
for msg in st.session_state.messages:
    if msg:
        if isinstance(msg, SystemMessage):
            st.chat_message("system").write(msg.content)
        elif isinstance(msg, AIMessage):
            st.chat_message("assistant").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)

if prompt := st.chat_input():   # Handle user input
    st.session_state.messages.append(HumanMessage(prompt))
    st.chat_message("user").write(prompt)

    # Stream the AI response
    response = get_ai_response(st.session_state["messages"])
    
    result = st.chat_message("assistant").write_stream(response) # Output AI message
    # Append AI message to session state
    st.session_state["messages"].append(AIMessage(result))
   
