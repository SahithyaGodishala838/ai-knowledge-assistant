![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![RAG](https://img.shields.io/badge/Architecture-RAG-purple)
![AI](https://img.shields.io/badge/AI-LLM%20%7C%20Embeddings-brightgreen)
![GitHub](https://img.shields.io/badge/Version_Control-GitHub-black)

# 🤖 AI Knowledge Assistant

*A Production-Ready Retrieval-Augmented Generation (RAG) System*


## 📌 Project Overview

**AI Knowledge Assistant** is a Python-based **Retrieval-Augmented Generation (RAG)** application that allows users to ask natural language questions over their own documents (TXT, DOCX, PDF) and receive **accurate, explainable answers grounded in the source content**.

This project was built incrementally with a strong focus on:

* Clean architecture
* Explainability
* Extensibility
* Real-world, production-grade design patterns

---

## 🎯 What This Project Solves

Traditional LLMs:

* Hallucinate answers
* Cannot reason over private documents
* Lack source transparency

This assistant solves that by:

* Embedding user documents into a vector store
* Retrieving only the most relevant chunks
* Generating answers **strictly grounded in retrieved context**
* Showing **citations** for trust and explainability

---

## 🧠 Core Architecture (RAG Pipeline)

```
User Question
     ↓
Text Embedding
     ↓
Vector Search (Similarity Matching)
     ↓
Relevant Chunks Retrieved
     ↓
Prompt Construction (with citations + memory)
     ↓
LLM / Local Generator
     ↓
Grounded Answer + Sources
```

---

## 🗂️ Supported Document Types

Documents are placed in:

```
data/documents/
```

Supported formats:

* `.txt`
* `.docx`
* `.pdf` (text-based)

---

## 🧩 Project Structure

```
ai-knowledge-assistant/
│
├── src/
│   ├── app.py                     # Stable CLI application
│   ├── app_advanced.py            # Advanced CLI with configurable RAG
│   ├── rag_pipeline.py            # Core RAG logic (stable)
│   ├── rag_pipeline_advanced.py   # Wrapper pipeline (add-on features)
│   ├── vector_store.py            # Embeddings storage + search
│   ├── embedder.py                # Text embedding logic
│   ├── chunker.py                 # Text chunking logic
│   ├── document_loader.py         # TXT / DOCX / PDF loader
│   └── llm_providers.py           # OpenAI / Gemini / HF / Local generators
│
├── app_streamlit.py               # Stable Streamlit web app
├── app_streamlit_advanced.py      # Advanced Streamlit UI
│
├── data/
│   └── documents/                # User documents
│
├── storage/
│   └── vectors.json              # Vector embeddings
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Features Implemented (Day-by-Day)

---

### ✅ Day 1–2: Project Setup & Foundations

* Python project setup
* Git & GitHub integration
* Clean folder structure
* First CLI execution

---

### ✅ Day 3: Document Ingestion & Chunking

* Load `.txt` documents
* Chunk text into semantically meaningful pieces
* Prepare data for embeddings

---

### ✅ Day 4: Embeddings & Vector Store

* Generate embeddings for document chunks
* Store vectors in JSON-based vector store
* Perform cosine similarity search

---

### ✅ Day 5: Full RAG System

* End-to-end RAG pipeline
* Query → Retrieve → Generate
* Multi-LLM support:

  * OpenAI
  * Gemini
  * HuggingFace
  * Local (no API)

---

### ✅ Day 6: UX & Explainability

* Improved retrieval quality
* Source visibility (document + similarity)
* Streamlit UI for web interaction

---

### ✅ Day 7: Advanced, Production-Grade Features

#### 🅰️ Chat Memory (Conversation Context)

* Multi-turn conversation support
* Follow-up questions like *“Explain them”* work correctly
* Session-level memory (safe & controlled)

#### 🅱️ Source Citations

* Answers include document + chunk references
* Improves trust and explainability
* Enterprise-ready AI pattern

#### 🅲 Advanced RAG Controls (Add-On)

* Configurable parameters:

  * Top-K chunks
  * Similarity threshold
* Implemented via **wrapper pipeline** (no breaking changes)

#### 🅳 Advanced Streamlit UI (Add-On)

* Sidebar controls for RAG tuning
* Clean UI (no experimental labels)
* Separate advanced entry point

---

## 🔁 Stable vs Advanced Design (Important)

This project intentionally separates:

### 🔹 Stable Entry Points

* `src/app.py`
* `app_streamlit.py`

### 🔹 Advanced Entry Points (Add-Ons)

* `src/app_advanced.py`
* `app_streamlit_advanced.py`
* `src/rag_pipeline_advanced.py`

👉 This allows experimentation **without breaking production logic** — a real-world engineering pattern.

---

## ▶️ How to Run the Project

### 🔹 Build the Vector Index

```bash
python src/build_index.py all
```

---

### 🔹 Run Stable CLI

```bash
python src/app.py
```

---

### 🔹 Run Advanced CLI

```bash
python src/app_advanced.py
```

---

### 🔹 Run Stable Streamlit App

```bash
streamlit run app_streamlit.py
```

---

### 🔹 Run Advanced Streamlit App

```bash
streamlit run app_streamlit_advanced.py
```

---

## 🧪 Example Questions

* *What are my core technical skills?*
* *Explain them in simple words*
* *What projects have I worked on?*
* *Summarize my resume*

---

## 🧠 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Embeddings & vector similarity search
* Chunking strategies
* Multi-document reasoning
* Explainable AI (citations)
* Chat memory
* Wrapper-based extensibility
* Clean Git practices

---


## 👤 Author

**Sahithya Godishala**
AI / ML Engineer
📍 United States


