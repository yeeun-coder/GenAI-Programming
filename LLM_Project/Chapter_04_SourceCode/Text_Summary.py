from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_Key)

# Function to summarize text file
def fSummarize_txt(file_path: str): 
    client = OpenAI(api_key=strGPT_API_Key)

    # Read the given text file
    with open(file_path, 'r', encoding='utf-8') as f:
        txtDocument = f.read()

    # Create system prompt for summarization
    system_prompt = f'''
    You are a bot that summarizes the following text. Read the text below, identify the author's problem and argument, and summarize the main points.

    Format to be written is as follows.
    
    # Title

    ## Author's problem identification and argument (within 15 sentences)
    
    ## Introduction Author

    =============== [ Text Below ] ===============
    { txtDocument }
    '''
    print(system_prompt)
    print('=========================================')

    # Create summary using OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.1,
        messages=[
            {"role": "system", "content": system_prompt},
        ]
    )
    return response.choices[0].message.content 

if __name__ == '__main__':
    file_path = './data/KSCI_Paper_with_preprocessing.txt'

    PDF_Summary = fSummarize_txt(file_path)
    print(PDF_Summary)

    # Save the summarized content to a file
    with open('./data/Paper_summary.txt', 'w', encoding='utf-8') as f:
        f.write(PDF_Summary)

