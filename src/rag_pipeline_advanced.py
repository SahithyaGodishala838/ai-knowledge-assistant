from rag_pipeline import rag_answer as base_rag_answer

def rag_answer(
    question,
    provider="openai",
    top_k=5,
    min_similarity=0.20,
    chat_history=None,
    fallback_chunks=None
):
    """
    Advanced wrapper:
    - Accepts min_similarity and fallback_chunks (even if base rag_answer doesn't)
    - Calls your existing rag_answer safely
    """

    try:
        # If your base rag_answer already supports these args, great
        return base_rag_answer(
            question,
            provider=provider,
            top_k=top_k,
            min_similarity=min_similarity,
            chat_history=chat_history,
            fallback_chunks=fallback_chunks
        )
    except TypeError:
        # Otherwise, call base version with only supported args
        return base_rag_answer(
            question,
            provider=provider,
            top_k=top_k,
            chat_history=chat_history
        )
