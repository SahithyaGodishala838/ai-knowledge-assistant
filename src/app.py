from loader import load_text_documents


def main():
    print("👋 Hi Sahi, welcome back to your AI Knowledge Assistant project!")
    print("Day 2: Loading documents from data/documents")
    print("-" * 60)

    # Load text documents
    docs = load_text_documents()

    if not docs:
        print("No text documents found. Please add files to data/documents.")
        return

    print(f"Loaded {len(docs)} document(s):\n")
    for idx, doc in enumerate(docs, start=1):
        preview = doc["content"][:80].replace("\n", " ")
        print(f"{idx}. {doc['name']} → {preview}...")


if __name__ == "__main__":
    main()
