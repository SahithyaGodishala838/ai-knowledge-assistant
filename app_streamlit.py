import sys
from pathlib import Path

# Add project root and src/ to Python import path
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import streamlit as st
from rag_pipeline import rag_answer


st.set_page_config(page_title="AI Knowledge Assistant", layout="wide")

st.title("🤖 AI Knowledge Assistant")
st.caption("Your RAG-based assistant over TXT/PDF/DOCX documents")

with st.sidebar:
    st.header("Settings")
    provider = st.selectbox("LLM Provider", ["local", "openai", "gemini", "huggingface"])
    top_k = st.slider("Top K Chunks", 1, 10, 5)
    st.info("Tip: Use 'local' if you don’t have API keys configured.")

question = st.text_input("Ask a question:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        answer, retrieved = rag_answer(question, provider=provider, top_k=top_k)

        st.subheader("💡 Answer")
        st.write(answer)

        st.subheader("📘 Sources (Retrieved Chunks)")
        if not retrieved:
            st.write("No chunks retrieved.")
        else:
            for r in retrieved:
                st.markdown(f"**{r['doc_name']}** | similarity: `{r['similarity']:.4f}`")
                st.write(r["text"][:600] + ("..." if len(r["text"]) > 600 else ""))
                st.divider()
