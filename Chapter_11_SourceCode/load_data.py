import os
from langchain_core.documents import Document

# Find .txt files in the folder_path, read their contents, and save them to a list.
def load_documents(folder_path):
    docs = []
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found...: {folder_path}")

    for file in os.listdir(folder_path):
        if file.endswith(".txt"):            
            file_path = os.path.join(folder_path, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    docs.append(Document(page_content=content, metadata={"source": file}))
            except Exception as e:
                print(f"File read error...: {file_path} -> {e}")

    return docs

