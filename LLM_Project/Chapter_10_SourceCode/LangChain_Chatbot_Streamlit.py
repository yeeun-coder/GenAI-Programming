import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

# LangChain Chatbot class using OpenAI models
from langchain_openai import ChatOpenAI  
# In-memory chat message history class from LangChain core
from langchain_core.chat_history import InMemoryChatMessageHistory  
# Runnable wrapper class to use message history with LangChain runnables
from langchain_core.runnables.history import RunnableWithMessageHistory  
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()

# Input api_key in the sidebar
#with st.sidebar:
#    strOpenAI_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
#client = OpenAI(api_key = strOpenAI_API_Key)

LLM = ChatOpenAI(model="gpt-4o-mini")   # Initialize LangChain Chatbot model

st.title("💬 Langchain Chatbot ")        # Streamlit UI
st.caption("🚀 A Streamlit Chatbot powered by OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage("너는 사용자의 질문에 친절이 답하는 AI 챗봇이다.")
    ]

# Initialize session state for storing chat history per session ID
if "store" not in st.session_state:
    st.session_state["store"] = {}

def get_session_history(session_id: str):
    if session_id not in st.session_state["store"]:
        st.session_state["store"][session_id] = InMemoryChatMessageHistory()
    return st.session_state["store"][session_id]

with_message_history = RunnableWithMessageHistory(LLM, get_session_history)

config = {"configurable": {"session_id": "Inhatc"}}

# Display chat messages from session state in the Streamlit UI
for msg in st.session_state.messages:
    if msg:
        if isinstance(msg, SystemMessage):
            st.chat_message("system").write(msg.content)
        elif isinstance(msg, AIMessage):
            st.chat_message("assistant").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)

if prompt := st.chat_input():
    print('user:', prompt)  
    st.session_state.messages.append(HumanMessage(prompt))
    st.chat_message("user").write(prompt)

    # Invoke the LangChain chatbot with the user's message and session config
    response = with_message_history.invoke([HumanMessage(prompt)], config=config)

    msg = response.content
    st.session_state.messages.append(response)
    st.chat_message("assistant").write(msg)
    print('assistant:', msg) 
   
