from loader import load_text_documents
from embedder import embed_documents


def main():
    print("👋 Day 3: Generating embeddings for your documents!")
    print("-" * 60)

    # Step 1 — Load documents
    docs = load_text_documents()

    if not docs:
        print("No documents found. Add files in data/documents.")
        return

    print(f"Loaded {len(docs)} document(s). Now generating embeddings...\n")

    # Step 2 — Generate embeddings
    embedded_docs = embed_documents(docs)

    # Step 3 — Show embedding size for confirmation
    for idx, doc in enumerate(embedded_docs, start=1):
        print(f"{idx}. {doc['name']} → Embedding length: {len(doc['embedding'])}")

    print("\n🎉 Embeddings generated successfully!")
    print("Tomorrow we will save them & perform semantic search.")
    

if __name__ == "__main__":
    main()
