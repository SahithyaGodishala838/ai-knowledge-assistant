from loader import load_text_documents
from embedder import embed_text
from chunker import chunk_text
from vector_store import save_vectors, load_vectors, search


def main():
    print("👋 Day 4: Chunking, Embeddings & Semantic Search")
    print("-" * 60)

    # 1. Load docs
    docs = load_text_documents()
    if not docs:
        print("No documents found.")
        return

    all_vectors = []

    # 2. Process each document
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

    # 3. Save vectors to disk
    save_vectors(all_vectors)

    # 4. Load vectors for search
    vectors = load_vectors()

    # 5. Test search
    query = "What did I write about learning AI?"
    print(f"\nSearching for: '{query}'")

    query_embedding = embed_text(query)
    results = search(query_embedding, vectors, top_k=3)

    print("\nTop Results:")
    for r in results:
        print(f"\n📌 Document: {r['doc_name']}")
        print(f"Chunk ID: {r['chunk_id']}")
        print(f"Score: {r['similarity']:.4f}")
        print(f"Text Snippet: {r['text'][:100]}...")


if __name__ == "__main__":
    main()
