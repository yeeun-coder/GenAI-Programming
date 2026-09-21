from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_Key)

# Create a chat completion
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "2026년 월드컵 우승팀은 어디야?"}
    ]
)

print(response)

print('===[ Response Content ]===')
print(response.choices[0].message.content)
