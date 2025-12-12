from embedder import embed_text
from vector_store import load_vectors, search
from llm_providers import generate_with_provider

def build_chat_context(chat_history, max_turns=4):
    """
    Builds a short conversation context from recent turns.
    """
    if not chat_history:
        return ""

    recent = chat_history[-max_turns:]
    lines = []
    for turn in recent:
        lines.append(f"User: {turn['question']}")
        lines.append(f"Assistant: {turn['answer']}")

    return "\n".join(lines)

def build_prompt(question, retrieved_chunks, chat_history=None):
    chat_context = build_chat_context(chat_history)

    context_blocks = []
    for i, r in enumerate(retrieved_chunks, 1):
        cite = f"[{r['doc_name']} - Chunk {r['chunk_id']}]"
        context_blocks.append(
           f"{cite}\n{r['text']}"
    )
    context_text = "\n\n".join(context_blocks)


    prompt = f"""
You are an AI assistant that must answer ONLY using the context below.
If the answer is not in the context, say "I don't know".

Conversation so far:
{chat_context}

Context:
{context_text}

Question:
{question}

Answer clearly and concisely:
""".strip()

    return prompt


def rag_answer(question, provider="openai", top_k=5, chat_history=None, fallback_chunks=None):

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
    retrieved = search(q_embed, vectors, top_k=top_k, min_similarity=0.20)

    if not retrieved and fallback_chunks:
       retrieved = fallback_chunks

    if not retrieved:
       return "I don't know (no relevant context found in your documents).", []


    # Step 4 — Build prompt for LLM
    prompt = build_prompt(question, retrieved, chat_history)

    # Step 5 — Generate answer
    print(f"🤖 Using provider: {provider}")
    answer = generate_with_provider(provider, prompt)

    return answer, retrieved
