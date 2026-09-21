from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_Key)

# Function to get AI response
def get_GPT_response(strMessages):
    response = client.chat.completions.create(
        model="gpt-4o",   
        temperature=0.9,  
        messages=strMessages,   
    )
    return response.choices[0].message.content  

strMessages = [ {"role": "system", "content": "너는 사용자를 도와주는 상담사야."}, ]

# Create a chat completion
while True:
    User_input = input("User: ")

    if User_input == "exit":  
        break 

    #Add user messages to conversation history
    strMessages.append({"role": "user", "content": User_input})  
    GPT_response = get_GPT_response(strMessages)  # Get GPT responses based on conversation history
    # Add GPT response to conversation history
    strMessages.append({"role": "assistant", "content": GPT_response}) 
    
    print("GPT: " + GPT_response) # Output GPT_response

