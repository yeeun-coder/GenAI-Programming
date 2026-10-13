from GPT_Timezone_Function import get_current_time, tools   # GPT_Timezone_Function.py
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import streamlit as st

load_dotenv()

# Input api_key in the sidebar
with st.sidebar:
    strOpenAI_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

client = OpenAI(api_key = strOpenAI_API_Key)         # Call OpenAI() method

# Function to get AI response
def get_AI_response(strMessages, strTools=None):
    response = client.chat.completions.create(
        model="gpt-4o",   
        messages=strMessages,   
        tools=strTools,             # Pass available tools
    )
    return response

st.title("💬 Chatbot")                 # Streamlit UI
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [   # Initial message of st.session_state
        {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},  
    ] 

for msg in st.session_state.messages:
    if msg["role"] in ["assistant", "user"]:  # Only for assistant or user messages
        st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input("Message를 입력하세요."):   # Chat User input
    # Append user message to conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})  
    st.chat_message("user").write(user_input)  # User message to browser output

    # Show loading spinner
    with st.spinner("AI is thinking..."):
        AI_response = get_AI_response(st.session_state.messages, tools)

    # Validate AI_response structure
    if AI_response.choices and hasattr(AI_response.choices[0], "message"):
        AI_message = AI_response.choices[0].message
    else:
        AI_message = {"content": "No AI response... please try again."}

    # Check for tool_calls in AI response    
    tool_calls = AI_message.tool_calls          # AI Response tool_calls
    if tool_calls:                              # If tool_calls exist
        for tool_call in tool_calls:
            tool_name = tool_call.function.name # Extract function name 
            tool_call_id = tool_call.id         # Tool_call ID    
            
            # String -> Dictionary
            arguments = json.loads(tool_call.function.arguments)  

            # Add function execution result to session state
            if tool_name == "get_current_time":     # tool_name="get_current_time"
                st.session_state.messages.append({
                    "role": "function",             # Set role to "function"
                    "tool_call_id": tool_call_id,
                    "name": tool_name,
                    "content": get_current_time(timezone=arguments['timezone']),  
                })
                
        # Add system message after tool execution
        st.session_state.messages.append({"role": "system", 
                                          "content": "이제 주어진 결과를 바탕으로 답변한다."})  

        # Get final AI response after tool execution
        with st.spinner("Organizing answers based on AI results..."):
            AI_response = get_AI_response(st.session_state.messages)
        AI_message = AI_response.choices[0].message

    # Append AI_message.content to session state
    st.session_state.messages.append({"role": "assistant", 
                                      "content": AI_message.content })  

    # Display AI response to browser
    st.chat_message("assistant").write(AI_message.content)  

