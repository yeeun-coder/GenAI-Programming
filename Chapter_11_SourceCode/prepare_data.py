# prepare_data.py
from typing import Any
from load_data import load_documents
from clean_data import clean_text


# Python-docx Document (For docx files)
try:
    from docx import Document as DocxDocument
except Exception:
    DocxDocument = None             # In case it is not installed

def _to_text(doc: Any) -> str:
    """
    Convert various document types to strings.
    Support:
      - str : String
      - bytes : UTF-8 decoding
      - LangChain Document : Using .page_content
      - python-docx Document : Combine paragraphs into text
      - etc : Convert to string with str(doc)
    """
    if doc is None:
        return ""

    if isinstance(doc, str):
        return doc

    if isinstance(doc, bytes):
        try:
            return doc.decode("utf-8", errors="ignore")
        except Exception:
            return doc.decode("latin-1", errors="ignore")

    # LangChain Document-like
    if hasattr(doc, "page_content"):
        try:
            return getattr(doc, "page_content")
        except Exception:
            pass            # Fallback down

    # Python-docx Document
    if DocxDocument is not None and isinstance(doc, DocxDocument):
        try:
            return "\n".join(p.text for p in doc.paragraphs)
        except Exception:
            pass            # Fallback

    # Fallback: String representation 
    return str(doc)

def prepare_docs(folder_path="C:/LLM_Project/Data/Text/"):
    """
    Loads a document from a folder, normalizes it to a string, and returns it as clean text.
    """
    raw_docs = load_documents(folder_path)

    # Debug: Check what type is coming in
    first_five = [type(d).__name__ for d in raw_docs[:5]]
    type_counts = {}
    for d in raw_docs:
        t = type(d).__name__
        type_counts[t] = type_counts.get(t, 0) + 1
    print(f"[DEBUG] First 5 loaded types: {first_five}")
    print(f"[DEBUG] Loaded document types: {type_counts}")

    # Normalize to string
    normalized_docs = [_to_text(doc) for doc in raw_docs]

    # Convert to Clean Text
    cleaned_docs = [clean_text(text) for text in normalized_docs]

    print(f"Prepared {len(cleaned_docs)} documents.")
    return cleaned_docs


