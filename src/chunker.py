import re
from typing import List


def split_into_sentences(text: str) -> List[str]:
    """
    Simple sentence splitter using regex.
    Not perfect, but much better than raw character slicing.
    """
    text = " ".join(text.split())  # normalize whitespace
    # Split on . ! ? followed by space (basic heuristic)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s.strip() for s in sentences if s.strip()]


def chunk_text(text: str, max_chars: int = 600, overlap_sentences: int = 2) -> List[str]:
    """
    Build chunks by grouping sentences up to max_chars.
    Adds overlap (last N sentences) to preserve context across chunks.
    """
    sentences = split_into_sentences(text)
    if not sentences:
        return []

    chunks = []
    current = []

    for s in sentences:
        # if adding this sentence exceeds max, finalize chunk
        if current and (sum(len(x) for x in current) + len(current) + len(s)) > max_chars:
            chunk = " ".join(current).strip()
            chunks.append(chunk)

            # overlap: carry last N sentences forward
            current = current[-overlap_sentences:] if overlap_sentences > 0 else []

        current.append(s)

    # final chunk
    if current:
        chunks.append(" ".join(current).strip())

    return chunks
