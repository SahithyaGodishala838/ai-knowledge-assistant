def chunk_text(text, max_length=300):
    """
    Splits text into chunks of approximately max_length characters.
    This is a simple approach for now — we improve later if needed.
    """
    chunks = []
    
    # Remove extra spaces/newlines
    cleaned = " ".join(text.split())

    # Create chunks
    for i in range(0, len(cleaned), max_length):
        chunk = cleaned[i:i+max_length]
        chunks.append(chunk)

    return chunks
