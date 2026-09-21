from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_Key)

# Create a chat completion
response = client.chat.completions.create(
  model="gpt-4o",   # GPT model
  temperature=0.9,  # 0~1 (0: 정확한 답변, 1: 창의적인 답변)
  messages=[
    {"role": "system", "content": "너는 배트맨에 나오는 조커야. 조커의 악당 캐릭터에 맞게 답변해줘."},
    {"role": "user", "content": "세상에서 누가 제일 예쁘니?"},
  ]	# Dictionary list(role, content)
    # system: GPT 역할, user: 사용자, assistant: GPT 답변 
)

print('====[ Response Content ]====')	
print(response.choices[0].message.content) # GPT 답변 출력

