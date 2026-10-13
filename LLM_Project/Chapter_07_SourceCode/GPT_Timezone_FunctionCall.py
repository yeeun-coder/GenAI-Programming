from GPT_Timezone_Function import get_current_time, tools   # GPT_Timezone_Function.py
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
strOpenAI_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strOpenAI_API_Key)

# Function to get AI response
def get_AI_response(strMessages, strTools=None):
    response = client.chat.completions.create(
        model="gpt-4o",   
        messages=strMessages,   
        tools=strTools,             # Pass available tools
    )
    return response

messages = [                        # Starting system message
    {"role": "system", "content": "너는 User를 도와주는 상담사야."},  
]

while True:
    user_input = input("User\t: ")  # User input
    if user_input == "exit":        # User wants to exit
        break
    
    # User message added to conversation history    
    messages.append({"role": "user", "content": user_input})  
    AI_response = get_AI_response(messages, tools)
    AI_message = AI_response.choices[0].message
    # print(AI_message)                             # AI response for debugging

    tool_calls = AI_message.tool_calls              # AI Response tool_calls
    if tool_calls:                                  # If tool_calls exist
        tool_name = tool_calls[0].function.name     # Extract function name 
        tool_call_id = tool_calls[0].id             # Tool_call ID    
       
        arguments = json.loads(tool_calls[0].function.arguments)  # String -> Dictionary

        if tool_name == "get_current_time":         # tool_name="get_current_time"
            messages.append({
                "role": "function",                 # Set role to "function"
                "tool_call_id": tool_call_id,
                "name": tool_name,
                                                    # content=get_current_time() with timezone
                "content": get_current_time(timezone=arguments['timezone']),  
            })
        AI_response = get_AI_response(messages, tools) 
        AI_message = AI_response.choices[0].message

    messages.append(AI_message)           # Append AI_message to messages
    print("AI\t: " + AI_message.content)  # Print AI response

