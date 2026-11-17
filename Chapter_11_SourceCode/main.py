# pip install -U sentence_transformers
# Data preparation
from prepare_data import prepare_docs
from split_text import split_docs

# Embedding and storage
from create_embeddings import get_embeddings
from store_faiss import build_faiss_index, save_metadata

# Retrieval and answer generation
from generate_answer import generate_answer

def run_pipeline():
    """
    Runs the full end-to-end RAG workflow.
    """
    print("\n[1/5] Load and Clean Data:")
    documents = prepare_docs("../LLM_Project/Data/Text/")    
    print(f"Loaded {len(documents)} clean documents.\n")

    print("[2/5] Split Text into Chunks:")
    # documents is a list of strings, but split_docs expects a list of documents
    # For this simple example where documents are small, we pass them as strings
    chunks_as_text = split_docs(documents, chunk_size=500, chunk_overlap=100)
    # In this case, chunks_as_text is a list of LangChain Document objects
    # Extract text content from LangChain Document objects
    texts = [c.page_content for c in chunks_as_text]
    print(f"Created {len(texts)} text chunks.\n")

    print("[3/5] Generate Embeddings:")
    embeddings = get_embeddings(texts)
  
    print("\n [4/5] Store Embeddings in FAISS:")
    index = build_faiss_index(embeddings)   # should create FAISS index of dimension 

    save_metadata(texts)                    # # Save metadata in the same order as embeddings
    print("Stored embeddings and metadata successfully.\n")

    print("[5/5] Retrieve & Generate Answer:")
    query = "Does unsupervised ML cover regression tasks?"

    # Pass index and texts to generate_answer, unless it loads from disk internally
    answer = generate_answer(query) #index=index, texts=texts, top_k=3
    print("Answer:\n", answer)

if __name__ == "__main__":
    run_pipeline()
    
