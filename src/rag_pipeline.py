from embedder import embed_text
from vector_store import load_vectors, search
from llm_providers import generate_with_provider


def build_prompt(question: str, retrieved):
    """
    Build a context + question prompt for RAG.
    """
    context_sections = []
    for idx, item in enumerate(retrieved, start=1):
        context_sections.append(
            f"Chunk {idx} from {item['doc_name']}:\n{item['text']}\n"
        )

    context = "\n".join(context_sections)

    prompt = f"""
You are an AI assistant that must answer ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer clearly and concisely:
"""
    return prompt.strip()


def rag_answer(question: str, provider: str = "openai", top_k: int = 5):
    """
    Full RAG pipeline.
    """
    print(f"\n🔍 Retrieving relevant information for: '{question}'")

    # Step 1 — Load stored vectors
    vectors = load_vectors()
    if not vectors:
        return "[Error: No vectors found. Run build_index.py first.]"

    # Step 2 — Embed question
    q_embed = embed_text(question)

    # Step 3 — Retrieve top chunks
    retrieved = search(q_embed, vectors, top_k=5, min_similarity=0.20)


    # Step 4 — Build prompt for LLM
    prompt = build_prompt(question, retrieved)

    # Step 5 — Generate answer
    print(f"🤖 Using provider: {provider}")
    answer = generate_with_provider(provider, prompt)

    return answer, retrieved
