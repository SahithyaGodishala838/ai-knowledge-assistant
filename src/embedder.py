from sentence_transformers import SentenceTransformer

# Load embedding model (lightweight & fast)
MODEL_NAME = "all-MiniLM-L6-v2"

# Load only once (for performance)
embedding_model = SentenceTransformer(MODEL_NAME)


def embed_text(text: str):
    """
    Convert a single text string into an embedding vector.
    """
    return embedding_model.encode(text).tolist()


def embed_documents(documents):
    """
    Convert a list of documents (each with 'name' & 'content')
    into embeddings.
    Returns:
        [
            {
                "name": "note1.txt",
                "content": "full text here...",
                "embedding": [0.25, -0.11, ...]
            },
            ...
        ]
    """
    results = []
    for doc in documents:
        vector = embed_text(doc["content"])
        results.append({
            "name": doc["name"],
            "content": doc["content"],
            "embedding": vector
        })
    return results
