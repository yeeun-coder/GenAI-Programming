from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# documents must be a List[Document].
def split_docs(documents, chunk_size=500, chunk_overlap=100):
   
   # Define the splitter
   splitter = RecursiveCharacterTextSplitter(
       chunk_size=chunk_size,
       chunk_overlap=chunk_overlap
   )

   # Use the splitter to split docs into chunks
   chunks = splitter.create_documents(documents)
   print(f"Total chunks created: {len(chunks)}")

   return chunks

