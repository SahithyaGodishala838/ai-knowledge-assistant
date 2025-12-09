from rag_pipeline import rag_answer

def main():
    print("\n🤖 Welcome to Your AI Knowledge Assistant!")
    print("Day 5: Full RAG Q&A System Online")
    print("-" * 60)

    print("\nAvailable LLM Providers:")
    print("1. openai")
    print("2. gemini")
    print("3. huggingface")
    print("4. local")

    provider = input("\nChoose a provider (openai/gemini/huggingface/local): ").strip().lower()

    while True:
        question = input("\n❓ Ask a question (or type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\n👋 Goodbye Sahi! See you in Day 6.")
            break

        answer, retrieved = rag_answer(question, provider=provider)

        print("\n📘 Retrieved Chunks:")
        for r in retrieved:
            print(f"- {r['doc_name']} | Similarity: {r['similarity']:.4f}")
            print(f"  Text: {r['text'][:120]}...\n")

        print("\n💡 AI Answer:\n")
        print(answer)
        print("\n" + "="*60)

if __name__ == "__main__":
    main()
