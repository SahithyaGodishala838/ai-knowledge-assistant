from loader import load_text_documents
from embedder import embed_text
from chunker import chunk_text
from vector_store import save_vectors, load_vectors, search


def main():
    print("🔧 Building vector index from documents...")
    print("-" * 50)

    docs = load_text_documents()
    if not docs:
        print("No documents found in data/documents.")
        return

    all_vectors = []

    for doc in docs:
        chunks = chunk_text(doc["content"], max_length=300)
        for idx, chunk in enumerate(chunks):
            embedding = embed_text(chunk)
            all_vectors.append({
                "doc_name": doc["name"],
                "chunk_id": idx,
                "text": chunk,
                "embedding": embedding
            })

    save_vectors(all_vectors)

    # Optional quick test
    test_query = "What did I write about learning AI?"
    print(f"\nTesting search for query: '{test_query}'")
    vectors = load_vectors()
    q_embed = embed_text(test_query)
    results = search(q_embed, vectors, top_k=3)

    print("\nTop results:")
    for r in results:
        print(f"- {r['doc_name']} | sim={r['similarity']:.4f}")
        print(f"  Text: {r['text'][:120]}...\n")


if __name__ == "__main__":
    main()
