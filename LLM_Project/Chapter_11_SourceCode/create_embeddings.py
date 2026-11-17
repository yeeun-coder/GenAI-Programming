# pip install --index-url https://download.pytorch.org/whl/cpu torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1
# pip install -U sentence_transformers
from sentence_transformers import SentenceTransformer 
import numpy as np

# Load embedding model: If you have a GPU, device='cuda'
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cuda')

def get_embeddings(text_chunks):  
   print(f"Creating embeddings for {len(text_chunks)} chunks:")
   embeddings = model.encode(text_chunks, show_progress_bar=True)
  
   print(f"Embeddings shape: {embeddings.shape}")
   return np.array(embeddings)

