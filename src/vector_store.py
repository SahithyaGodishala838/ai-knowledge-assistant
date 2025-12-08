import json
import numpy as np
from pathlib import Path


STORE_PATH = Path(__file__).resolve().parents[1] / "storage"
STORE_PATH.mkdir(exist_ok=True)
VECTOR_FILE = STORE_PATH / "vectors.json"


def save_vectors(vectors):
    """
    Save list of dictionaries:
    [
      {
        "doc_name": ...,
        "chunk_id": ...,
        "text": ...,
        "embedding": [...]
      }
    ]
    """
    with open(VECTOR_FILE, "w", encoding="utf-8") as f:
        json.dump(vectors, f, indent=2)
    print(f"Saved {len(vectors)} vectors to {VECTOR_FILE}")


def load_vectors():
    if not VECTOR_FILE.exists():
        print("[WARNING] No vector file found.")
        return []
    with open(VECTOR_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def cosine_similarity(vec1, vec2):
    """Compute cosine similarity between two embeddings."""
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search(query_embedding, vectors, top_k=3):
    """Return top_k most similar chunks."""
    results = []

    for v in vectors:
        sim = cosine_similarity(query_embedding, v["embedding"])
        results.append({
            "doc_name": v["doc_name"],
            "chunk_id": v["chunk_id"],
            "text": v["text"],
            "similarity": float(sim)
        })

    # Sort by similarity, highest first
    results = sorted(results, key=lambda x: x["similarity"], reverse=True)

    return results[:top_k]
