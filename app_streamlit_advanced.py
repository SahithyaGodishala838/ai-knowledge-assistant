import sys
from pathlib import Path
import streamlit as st

# Keep your existing import approach (no changes to app_streamlit.py)
ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from rag_pipeline_advanced import rag_answer

st.set_page_config(page_title="AI Knowledge Assistant (Day 7+)", layout="wide")
st.title("🤖 AI Knowledge Assistant ")
st.caption("Same project, extra controls added as optional add-on entrypoint")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_retrieved" not in st.session_state:
    st.session_state.last_retrieved = []

with st.sidebar:
    st.header("Settings ")
    provider = st.selectbox("LLM Provider", ["local", "openai", "gemini", "huggingface"])
    top_k = st.slider("Top K Chunks", 1, 10, 5)
    min_similarity = st.slider("Min Similarity", 0.0, 1.0, 0.20, 0.05)

question = st.text_input("Ask a question:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        answer, retrieved = rag_answer(
            question,
            provider=provider,
            top_k=top_k,
            min_similarity=min_similarity,
            chat_history=st.session_state.chat_history,
            fallback_chunks=st.session_state.last_retrieved
        )

        if retrieved:
            st.session_state.last_retrieved = retrieved

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

        st.session_state.chat_history.append({"question": question, "answer": answer})
        st.session_state.chat_history = st.session_state.chat_history[-6:]
