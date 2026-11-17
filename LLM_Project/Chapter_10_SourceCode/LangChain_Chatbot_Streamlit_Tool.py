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

from langchain_core.tools import tool
from datetime import datetime
import pytz

@tool       # @tool decorator uses langchain's tool system
def get_current_time(timezone: str, location: str) -> str:
    """ 현재 시각 반환 함수."""
    try: 
        tz = pytz.timezone(timezone)
        now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        result = f'{timezone} ({location}) 현재시각 {now}'
        print(result)
        return result
    except pytz.UnknownTimeZoneError:
        return f"알 수 없는 타임존: {timezone}"

# Binding tools to the LLM
tools = [get_current_time,]
tool_dict = {"get_current_time": get_current_time,}
LLM_with_tools = LLM.bind_tools(tools)

st.title("💬 Langchain Chatbot with @Tool")        # Streamlit UI
st.caption("🚀 A Streamlit Chatbot powered by OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        SystemMessage("너는 사용자의 질문에 친절이 답하는 AI 챗봇이다."),
        AIMessage("How can I help you?")
    ]

# Function to handle user messages and get AI response
def get_ai_response(messages):
    response = LLM_with_tools.stream(messages) # LLM.stream() -> LLM_with_tools.stream()
    
    gathered = None
    for chunk in response:
        yield chunk
        
        if gathered is None:   # Initialize gathered on first chunk
            gathered = chunk
        else:
            gathered += chunk
            
    if gathered.tool_calls:    # If there are tool calls in the gathered response
        st.session_state.messages.append(gathered)
        
        for tool_call in gathered.tool_calls:
            selected_tool = tool_dict[tool_call['name']]
            tool_msg = selected_tool.invoke(tool_call)  # Invoke the tool
            print(tool_msg, type(tool_msg))
            st.session_state.messages.append(tool_msg)
            
        # Recursively get AI response after tool call
        for chunk in get_ai_response(st.session_state.messages):
            yield chunk

# Display messages on the Streamlit screen
for msg in st.session_state.messages:
    if msg.content:
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
   
