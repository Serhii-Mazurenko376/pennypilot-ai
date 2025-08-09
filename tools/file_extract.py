from typing import BinaryIO
import pdfplumber
from docx import Document

def _clean(text: str) -> str:
    # Normalize whitespace and avoid None
    return "\n".join([line.rstrip() for line in (text or "").splitlines()]).strip()

def extract_text_from_file(uploaded_file) -> str:
    """
    Detect by extension and extract plaintext.
    Supports: .pdf, .docx, .txt
    """
    name = uploaded_file.name or ""
    ext = name.lower().rsplit(".", 1)[-1]

    try:
        if ext == "pdf":
            with pdfplumber.open(uploaded_file) as pdf:
                pages = []
                for page in pdf.pages:
                    t = page.extract_text() or ""
                    pages.append(t)
                return _clean("\n\n".join(pages))
        elif ext == "docx":
            doc = Document(uploaded_file)
            return _clean("\n".join(p.text for p in doc.paragraphs))
        elif ext == "txt":
            # Handle utf-8/latin fallbacks
            data = uploaded_file.read()
            try:
                return _clean(data.decode("utf-8"))
            except UnicodeDecodeError:
                return _clean(data.decode("latin-1", errors="ignore"))
        else:
            return f"Unsupported file type: {ext}"
    except Exception as e:
        return f"Error while reading file: {e}"
