from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key = strGPT_API_Key)

first_response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are an AI Developer."},
        {"role": "user", "content": "최근 AI trend에 대해 알려줘."},
    ],
    temperature=0.7,
    max_tokens=256,
)

first_response_text = first_response.choices[0].message.content

second_response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "최근 AI trend에 대해 알려줘."},
        {"role": "assistant", "content": first_response_text},
        {"role": "user", "content": "이 기술 중 가장 주목받는 기술은?"},
    ],
)

print('===[ Response Content ]===')
print(second_response.choices[0].message.content)
