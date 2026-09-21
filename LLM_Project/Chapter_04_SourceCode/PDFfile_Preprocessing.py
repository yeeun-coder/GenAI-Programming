import os
import pymupdf

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

