from rag_pipeline import rag_answer

def main():
    print("\n🤖 AI Knowledge Assistant (Day 7+ Add-on CLI)")
    print("-" * 60)

    print("\nAvailable LLM Providers:")
    print("1. openai")
    print("2. gemini")
    print("3. huggingface")
    print("4. local")

    provider = input("\nChoose a provider (openai/gemini/huggingface/local): ").strip().lower()

    # ✅ Add-on controls (do not touch src/app.py)
    top_k_in = input("Top K chunks (default 5): ").strip()
    min_sim_in = input("Min similarity (default 0.20): ").strip()

    top_k = int(top_k_in) if top_k_in else 5
    min_similarity = float(min_sim_in) if min_sim_in else 0.20

    chat_history = []
    last_retrieved = []

    while True:
        question = input("\n❓ Ask a question (or type 'exit' to quit): ").strip()

        if question.lower() == "exit":
            print("\n👋 Bye Sahi! (Day 7+ Add-on CLI)")
            break

        # Try calling rag_answer with add-on params.
        # If your rag_answer doesn't accept these yet, it will error.
        answer, retrieved = rag_answer(
            question,
            provider=provider,
            top_k=top_k,
            min_similarity=min_similarity,
            chat_history=chat_history,
            fallback_chunks=last_retrieved
        )

        if retrieved:
            last_retrieved = retrieved

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

        chat_history.append({"question": question, "answer": answer})
        chat_history = chat_history[-6:]


if __name__ == "__main__":
    main()
