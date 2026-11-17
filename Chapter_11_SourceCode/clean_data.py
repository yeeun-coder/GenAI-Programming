# clean_data.py
import re

def clean_text(text: str) -> str:
    # Keep letters/digits/whitespace and Hangul blocks; remove other symbols/emojis
    text = re.sub(r'[^\w\s\uAC00-\uD7A3\u1100-\u11FF\u3130-\u318F]+', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

