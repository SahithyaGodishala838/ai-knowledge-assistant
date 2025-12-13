from pathlib import Path
from typing import List, Dict

from pypdf import PdfReader
from docx import Document

import os

PROJECT_ROOT = Path(__file__).resolve().parents[1]

# APP_ENV controls which folder to read:
# - local  (default)  -> data/private_documents
# - public            -> data/documents
APP_ENV = os.getenv("APP_ENV", "local").strip().lower()

if APP_ENV == "public":
    DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"
else:
    DOCUMENTS_DIR = PROJECT_ROOT / "data" / "private_documents"


def _read_txt(file_path: Path) -> str:
    return file_path.read_text(encoding="utf-8", errors="ignore")


def _read_pdf(file_path: Path) -> str:
    reader = PdfReader(str(file_path))
    texts = []
    for page in reader.pages:
        t = page.extract_text() or ""
        texts.append(t)
    return "\n".join(texts).strip()


def _read_docx(file_path: Path) -> str:
    doc = Document(str(file_path))
    parts = [p.text for p in doc.paragraphs if p.text and p.text.strip()]
    return "\n".join(parts).strip()


def load_documents() -> List[Dict]:
    """
    Loads .txt, .pdf, .docx from data/documents.
    Returns: [{"name": "...", "content": "...", "type": "txt/pdf/docx"}]
    """
    docs = []

    if not DOCUMENTS_DIR.exists():
        print(f"[WARNING] Documents folder does not exist: {DOCUMENTS_DIR}")
        return docs

    supported = ["*.txt", "*.pdf", "*.docx"]
    files = []
    for pattern in supported:
        files.extend(DOCUMENTS_DIR.glob(pattern))

    for file_path in sorted(files):
        suffix = file_path.suffix.lower()

        try:
            if suffix == ".txt":
                content = _read_txt(file_path)
                doc_type = "txt"
            elif suffix == ".pdf":
                content = _read_pdf(file_path)
                doc_type = "pdf"
            elif suffix == ".docx":
                content = _read_docx(file_path)
                doc_type = "docx"
            else:
                continue

            # Skip empty extracts (common for scanned PDFs)
            if not content.strip():
                print(f"[WARNING] Extracted empty text from {file_path.name} (maybe scanned PDF). Skipping.")
                continue

            docs.append({
                "name": file_path.name,
                "content": content,
                "type": doc_type
            })

        except Exception as e:
            print(f"[ERROR] Failed to load {file_path.name}: {e}")

    return docs
