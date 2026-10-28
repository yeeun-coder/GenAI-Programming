from openai import OpenAI  
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()   # Get API key from .env file  
strGPT_API_Key = os.getenv('OPENAI_API_KEY')  

# Create an instance of ChatOpenAI
LLM = ChatOpenAI(model="gpt-4o")

# Initial system message
strMessages = [ SystemMessage("너는 사용자를 도와주는 상담사야."),]  

# Create a chat completion
while True:
    User_input = input("User: ")
    if User_input == "exit":  break 

    #Add user messages to conversation history
    strMessages.append(HumanMessage(User_input))  
    GPT_response = LLM.invoke(strMessages)  # Get GPT_responses 
    strMessages.append(GPT_response)        # Append GPT responses 
    
    print("GPT: " + GPT_response.content)   # Output GPT_response

