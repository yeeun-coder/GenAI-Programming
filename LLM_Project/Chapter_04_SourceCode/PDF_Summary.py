from openai import OpenAI
from dotenv import load_dotenv
import os
import pymupdf

load_dotenv()
strGPT_API_Key = os.getenv('OPENAI_API_KEY')  # Get API key from .env file  

# Call OpenAI() method
client = OpenAI(api_key = strGPT_API_Key)

def pdf_to_text(pdf_file_path: str): 
    # PDF file path
    pdf_file_path = "./data/KSCI_Paper.pdf"
    objDoc = pymupdf.open(pdf_file_path)

    header_height = 120    # Define header height(Case-by-case adjustments are required)
    footer_height = 150    # Define footer height(Case-by-case adjustments are required)
    full_text = ''         # Initialize full text variable

    # Extract text from each page
    for page in objDoc:
        rect = page.rect        # Get page dimensions
        
        header = page.get_text(clip=(0, 0, rect.width, header_height))
        footer = page.get_text(clip=(0, rect.height-footer_height, rect.width , rect.height))
        Contents = page.get_text(clip=(0, header_height, rect.width , rect.height-footer_height))

        full_text += Contents + '\n------------------------------------\n'

    # Get PDF file name without extension
    pdf_file_name = os.path.basename(pdf_file_path)
    pdf_file_name = os.path.splitext(pdf_file_name)[0] # Remove file extension

    # Save extracted text to "{pdf_file_path}_with_Preprocessing.txt" file
    txtFile_Name = f"./data/{pdf_file_name}_with_Preprocessing.txt"
    with open(txtFile_Name, 'w', encoding='utf-8') as f:
        f.write(full_text)
        
    return txtFile_Name

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

# Function to summarize PDF file
def fSummarize_pdf(pdf_file_path: str, output_file_path: str):
    txt_file_path = pdf_to_text(pdf_file_path)
    PDF_Summary = fSummarize_txt(txt_file_path)
    
    # Save the summarize pdf file to a text file(PDF_Paper_summary.txt)
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(PDF_Summary)
        
if __name__ == '__main__':
    pdf_file_path = './data/KSCI_Paper.pdf'
    PDF_Summary = fSummarize_pdf(pdf_file_path, './data/PDF_Paper_summary.txt')
