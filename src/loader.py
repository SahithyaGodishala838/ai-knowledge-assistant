import os
from pathlib import Path

# Locate the project root (1 level above src)
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Path to data/documents
DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"


def load_text_documents():
    """
    Load all .txt files from data/documents.
    Returns:
        A list of dicts:
        [
          {"name": "note1.txt", "content": "..."},
          ...
        ]
    """
    docs = []

    if not DOCUMENTS_DIR.exists():
        print(f"[WARNING] No documents directory found at: {DOCUMENTS_DIR}")
        return docs

    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            docs.append({
                "name": file_path.name,
                "content": content
            })
        except Exception as e:
            print(f"[ERROR] Failed to read {file_path.name}: {e}")

    return docs
