import os
import pymupdf

# PDF file path
pdf_file_path = "./data/KSCI_Paper.pdf"
objDoc = pymupdf.open(pdf_file_path)

full_text = ''                  # Initialize full text variable

for page in objDoc:             # Repeat document pages
    strText = page.get_text()   # Extract page text
    full_text += strText

# Get PDF file name without extension
pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0] # Remove file extension

# Save extracted text to "pdf_file_path.txt" file
txtFile_Name = f"./data/{pdf_file_name}.txt"
with open(txtFile_Name, 'w', encoding='utf-8') as f:
    f.write(full_text)
