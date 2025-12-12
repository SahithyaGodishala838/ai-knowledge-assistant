from rag_pipeline import rag_answer

def main():
    print("\n🤖 Welcome to Your AI Knowledge Assistant!")
    print("Day 7: Chat Memory Enabled")
    print("-" * 60)

    print("\nAvailable LLM Providers:")
    print("1. openai")
    print("2. gemini")
    print("3. huggingface")
    print("4. local")

    provider = input("\nChoose a provider (openai/gemini/huggingface/local): ").strip().lower()

    chat_history = []  # ✅ memory starts here (outside loop)
    last_retrieved = []

    while True:
        question = input("\n❓ Ask a question (or type 'exit' to quit): ").strip()

        if question.lower() == "exit":
            print("\n👋 Goodbye Sahi! See you in Day 7.")
            break

        # ✅ pass chat_history into rag pipeline
        answer, retrieved = rag_answer(
    question,
    provider=provider,
    chat_history=chat_history,
    fallback_chunks=last_retrieved
)

        if retrieved:
           last_retrieved = retrieved
        else:
            retrieved = last_retrieved

        print("\n📘 Retrieved Chunks:")
        if not retrieved:
            print("- (No chunks retrieved)\n")
        else:
            for r in retrieved:
                print(f"- {r['doc_name']} | Similarity: {r['similarity']:.4f}")
                print(f"  Text: {r['text'][:120]}...\n")

        print("\n💡 AI Answer:\n")
        print(answer)
        print("\n" + "=" * 60)

        # ✅ store this turn in memory AFTER getting the answer
        chat_history.append({
            "question": question,
            "answer": answer
        })

        # ✅ keep only last 6 turns (prevents prompt getting too long)
        chat_history = chat_history[-6:]


if __name__ == "__main__":
    main()
