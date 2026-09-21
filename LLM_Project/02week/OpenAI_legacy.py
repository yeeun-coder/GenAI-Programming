from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key = strGPT_API_Key)

response = completion = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="AI 기술의 미래에 대하여 알려줘.",
    temperature=0.7,
    max_tokens=150,
)

print('===[ Response Content ]===')
# print(response.choices[0].message.content)  # 오류
print(response.choices[0].text)
