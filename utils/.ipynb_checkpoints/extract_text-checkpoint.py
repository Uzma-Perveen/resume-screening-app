import io
import docx2txt
from PyPDF2 import PdfReader

def extract_from_docx(file_bytes: bytes) -> str:
    # docx2txt expects a path; workaround: write to temp if needed in Streamlit
    # In Streamlit we’ll save uploaded file to a NamedTemporaryFile.
    return docx2txt.process(file_bytes)  # (see app.py for temp file handling)

def extract_from_pdf(file) -> str:
    reader = PdfReader(file)
    pages = []
    for p in reader.pages:
        try:
            pages.append(p.extract_text() or "")
        except:
            pages.append("")
    return "\n".join(pages)
