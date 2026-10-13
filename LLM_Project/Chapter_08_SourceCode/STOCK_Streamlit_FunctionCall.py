from GPT_Multiple_Function import get_current_time, tools, get_yf_stock_info, get_yf_stock_history, get_yf_stock_recommendations
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import streamlit as st
from collections import defaultdict         # For default dictionary

load_dotenv()

# Input api_key in the sidebar
with st.sidebar:
    strOpenAI_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strOpenAI_API_Key)

# Function to get AI response
def get_AI_response(strMessages, strTools=None, bStream=True):
    response = client.chat.completions.create(
        model="gpt-4o", 
        stream=bStream,             # Enable streaming    
        messages=strMessages,   
        tools=strTools,             # Pass available tools
    )
    if bStream:
        for chunk in response:       # Stream response chunks
            yield   chunk            # Yield each chunk to the caller
    else:
        return response
    
# Function to convert tool list to tool object
def tool_list_to_tool_obj(tools):    
    tool_calls_dict = defaultdict(lambda: {"id": None, "function": {"arguments": "", "name": None}, "type": None})                # Default dictionary
   
    for tool_call in tools:                      # Tool function call iteration         
        if tool_call.id is not None:             # ID check    
            tool_calls_dict[tool_call.index]["id"] = tool_call.id

        if tool_call.function.name is not None:  # Function name check
            tool_calls_dict[tool_call.index]["function"]["name"] = tool_call.function.name

        # Add arguments
        tool_calls_dict[tool_call.index]["function"]["arguments"] += tool_call.function.arguments
    
        if tool_call.type is not None:           # Type check
            tool_calls_dict[tool_call.index]["type"] = tool_call.type
    
    tool_calls_list = list(tool_calls_dict.values())    # Convert dictionary to list
    return {"tool_calls": tool_calls_list}  
    
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
        AI_response = get_AI_response(st.session_state.messages, tools, bStream=True)

    content = ''
    tool_calls = None       # Initialize tool_calls 
    tool_calls_chunk = []   # Initialize tool_calls_chunk list
    
    # Empty assistant chat message for streaming
    with st.chat_message("assistant").empty(): 
        for chunk in AI_response:
            content_chunk = chunk.choices[0].delta.content      # Get content chunk
            if content_chunk: 
                print(content_chunk, end="")	# Print content chunk to console
                content += content_chunk        # Append to full content
                st.markdown(content)            # Streamlit chat message markdown output

            # If tool_calls exist in chunk then append to tool_calls_chunk list
            if chunk.choices[0].delta.tool_calls:	
                tool_calls_chunk += chunk.choices[0].delta.tool_calls  

        tool_obj = tool_list_to_tool_obj(tool_calls_chunk)      # Convert to tool_obj
        tool_calls = tool_obj["tool_calls"]                     # Extract tool_calls list

        if len(tool_calls) > 0:         # If tool_calls exist, display in st.write
            print(tool_calls)
            # Extract and display function information from  tool_calls
            tool_call_msg = [tool_call["function"] for tool_call in tool_calls]
            st.write(tool_call_msg) 

    print("\n=== End of AI response ===")

    if tool_calls:                                          # If tool_calls exist
        for tool_call in tool_calls:
            tool_name = tool_call["function"]["name"]       # Extract function name 
            tool_call_id = tool_call["id" ]                 # Tool_call ID    
            arguments = json.loads(tool_call["function"]["arguments"])  # String -> Dictionary

            # Add function execution result to session state
            if tool_name == "get_current_time":         
                Getfunction_result = get_current_time(timezone=arguments['timezone'])            
            elif tool_name == "get_yf_stock_info":     
                Getfunction_result = get_yf_stock_info(ticker=arguments['ticker'])
            elif tool_name == "get_yf_stock_history":  
                Getfunction_result = get_yf_stock_history(ticker=arguments['ticker'],period=arguments['period'])
            elif tool_name == "get_yf_stock_recommendations": 
                Getfunction_result = get_yf_stock_recommendations(ticker=arguments['ticker'])

            st.session_state.messages.append({
                "role": "function",                 # Set role to "function"
                "tool_call_id": tool_call_id,
                "name": tool_name,
                "content": Getfunction_result,      # Function execution result
            })
                         
        # Add system message after tool execution
        st.session_state.messages.append({"role": "system", "content": "이제 주어진 결과를 바탕으로 답변한다."})  

        # Get final AI response after tool execution
        with st.spinner(f"Executing {tool_name}..."):
            AI_response = get_AI_response(st.session_state.messages, tools, bStream=True)        

        content = ""
        with st.chat_message("assistant").empty():
            for chunk in AI_response:
                content_chunk = chunk.choices[0].delta.content
                if content_chunk:
                    print(content_chunk, end='')
                    content += content_chunk
                    st.markdown(content)        # Streamlit chat message markdown output

    # AI_message.content -> content
    st.session_state.messages.append({"role": "assistant", 
                                      "content": content })  

    print("AI\t: " + content)  # Print AI content to console

    # Display AI response to browser
    #st.chat_message("assistant").write(AI_message.content)  

