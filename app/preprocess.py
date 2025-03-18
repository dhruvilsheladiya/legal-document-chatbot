import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    """Extracts text from PDF using pdfplumber."""
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text.strip()

def perform_ner(text):
    """Performs Named Entity Recognition (NER) using spaCy."""
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

import chardet  # Install it using: pip install chardet

def read_file(file_path):
    """Reads a file while handling encoding errors."""
    with open(file_path, "rb") as f:
        raw_data = f.read()
    
    # Detect encoding
    result = chardet.detect(raw_data)
    encoding = result["encoding"] if result["encoding"] else "utf-8"

    # Try reading with detected encoding
    try:
        return raw_data.decode(encoding)
    except UnicodeDecodeError:
        return raw_data.decode("latin-1", errors="ignore")  # Fallback to "latin-1"
