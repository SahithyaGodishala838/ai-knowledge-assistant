# **## 🔥 Project Proposal: “Personal AI Knowledge Assistant” (RAG + LLM)**



\### ✨ What is it?



## **You’ll build a \*\*Personal AI Assistant\*\* that:**

## 

\* Reads \& stores your own documents (PDFs, text, notes).

\* Lets you \*\*chat\*\* with your knowledge (Q\&A).

\* Uses \*\*vector embeddings + retrieval + LLM\*\* → a real \*\*RAG (Retrieval-Augmented Generation)\*\* system.

\* Is written in \*\*Python\*\*, run from \*\*VS Code / Visual Studio\*\*, and fully tracked in \*\*GitHub\*\*.



This is \*\*exactly the trend now\*\*:



\* RAG

\* LLM-powered apps

\* AI assistants / copilots



And we’ll do it at a \*\*beginner-friendly speed\*\*, explaining \*every minute thing\*:



\* What a package is

\* Why we create a folder

\* What each line of code does

\* How Git/GitHub works

\* How the model “thinks”



---



#### **## 🧠 What You’ll Learn (Step-by-Step)**



From this one project, you’ll learn:



**1. \*\*Python basics in a real project\*\***



&nbsp;  \* Modules, packages, virtual environments

&nbsp;  \* `main.py`, imports, functions



**2. \*\*Modern AI Concepts\*\***



&nbsp;  \* Embeddings (turn text → vectors)

&nbsp;  \* Vector databases (similarity search)

&nbsp;  \* RAG pipeline: \*retrieve → augment → generate\*



**3. \*\*LLM Usage\*\***



&nbsp;  \* Calling an LLM API (e.g., OpenAI or local-like APIs)

&nbsp;  \* Crafting prompts

&nbsp;  \* Handling responses



**4. \*\*Project \& Dev Skills\*\***



&nbsp;  \* Clean folder structure

&nbsp;  \* Config files

&nbsp;  \* `requirements.txt`

&nbsp;  \* Git commits \& GitHub pushes



If you like, later we can add:



\* Simple \*\*FastAPI\*\* backend

\* Small \*\*Streamlit\*\* UI



But we’ll start with \*\*simple console app\*\*:



> You type a question → it reads from your docs → LLM answers with context.



---



**## 🏗️ Project Structure (What we’ll slowly build)**



We’ll end up with something like:



```text

ai-knowledge-assistant/

│

├── data/

│   └── documents/          # PDFs / txt files you want to chat with

│

├── storage/

│   └── embeddings/         # where vectors / index are stored

│

├── src/

│   ├── \_\_init\_\_.py

│   ├── config.py           # API keys, paths, model names

│   ├── loader.py           # load \& split documents

│   ├── embedder.py         # create embeddings

│   ├── vector\_store.py     # store \& search embeddings

│   ├── rag\_pipeline.py     # RAG logic: retrieve + generate

│   └── app.py              # simple CLI chatbot

│

├── .env                    # secrets (API keys) – not in git

├── .gitignore

├── requirements.txt

├── README.md

└── LICENSE (maybe later)

```



Don’t worry — we’ll create this \*\*piece by piece\*\*.



---



**## 🕒 1 Hour Per Day Plan (High-Level)**



I’ll be with you \*\*every day\*\*, giving you micro-tasks.



**### Week 1 – Setup + Fundamentals**



\* Day 1: Project folder, VS Code setup, Git/GitHub, virtual environment.

\* Day 2: `README`, `requirements.txt`, `.gitignore`, first commit.

\* Day 3: Create `src/` structure and a simple `app.py` that just prints “Hello Sahi”.

\* Day 4: Learn how to read a `.txt` file, print its content.

\* Day 5: Add a basic \*\*menu\*\* in `app.py` (e.g., 1) Ingest docs 2) Ask a question).



**### Week 2 – Document Loading \& Embeddings**



\* Learn what embeddings are (I’ll explain like a story).

\* Use a Python library (e.g., `sentence-transformers`) to generate embeddings.

\* Store them locally (maybe in `FAISS` or a simple pickle file).



**### Week 3 – Retrieval + LLM**



\* Implement similarity search.

\* Connect to LLM API (I’ll show you how to keep keys safe in `.env`).

\* Build the first real RAG pipeline: retrieve top-k chunks → send to LLM → answer.



**### Week 4 – Polish + Extras**



\* Improve prompting.

\* Handle errors.

\* Clean code structure.

\* Document everything in README.

\* Make it shiny for your portfolio.



---



**## 🎯 What We’ll Do \*\*Today\*\* (Session 1)**



Since you said: \*“explain each and every minute thing”\*, I’ll go \*\*super slow and clear\*\*.



**### ✅ Step 1: Create the Project Folder**



1\. Choose a location on your laptop (e.g., `Documents`).

2\. Create a folder: `ai-knowledge-assistant`

3\. Open \*\*VS Code / Visual Studio\*\*.

4\. Go to \*\*File → Open Folder\*\* → select `ai-knowledge-assistant`.



Now VS Code is “focused” on this project.



---



**### ✅ Step 2: Initialize Git**



Open the \*\*terminal\*\* in VS Code:



\* Top menu → `Terminal → New Terminal`.



You should see something like:



```bash

PS C:\\Users\\...\\ai-knowledge-assistant>

```



Run:



```bash

git init

```



What this means (in human terms):



\* You’re telling Git:



&nbsp; > “From now on, please track changes in this folder so I can commit and push them.”



---



**### ✅ Step 3: Create Basic Files**



In VS Code, create these files:



\#### 1. `README.md`



```markdown

\# AI Knowledge Assistant (RAG Project)



This project is a personal AI assistant that can read my documents and answer questions using Retrieval-Augmented Generation (RAG).



\- Built in Python

\- Developed in Visual Studio Code

\- Version-controlled with Git and GitHub



\## Goals



\- Learn modern AI concepts: embeddings, vector search, RAG, LLMs

\- Practice clean project structure and best practices

\- Spend ~1 hour daily making consistent progress

```



\#### 2. `.gitignore`



Create a file called `.gitignore` and add:



```gitignore

\_\_pycache\_\_/

\*.pyc

.env

.venv/

env/

.ipynb\_checkpoints

storage/

```



Explanation (briefly):



\* `\_\_pycache\_\_/`, `\*.pyc` → Python’s temporary compiled files. We don’t want them in Git.

\* `.env` → will contain secrets (API keys).

\* `.venv/` → virtual environment folder.

\* `storage/` → will hold embeddings / indexes; can be regenerated.



\#### 3. `requirements.txt`



Create `requirements.txt`:



```text

pandas

numpy

sentence-transformers

faiss-cpu

python-dotenv

openai

tqdm

```



We might tweak later, but this is our base.



---



**### ✅ Step 4: Create `src/` and `app.py`**



1\. Create a folder: `src`

2\. Inside `src`, create two files:



&nbsp;  \* `\_\_init\_\_.py` (leave it empty for now)

&nbsp;  \* `app.py`



Put this in `app.py`:



```python

def main():

&nbsp;   print("👋 Hi Sahi, welcome to your AI Knowledge Assistant project!")

&nbsp;   print("This is the starting point of our app.")

&nbsp;   print("We'll slowly turn this into a real RAG-based assistant.")



if \_\_name\_\_ == "\_\_main\_\_":

&nbsp;   main()

```



Explanation:



\* `def main():` → defines a function called `main`.

\* `if \_\_name\_\_ == "\_\_main\_\_":` → tells Python:



&nbsp; > “If you run this file directly (not imported), run `main()`.”



---



**### ✅ Step 5: Run the App Once**



In the terminal:



```bash

python src/app.py

```



You should see:



```text

👋 Hi Sahi, welcome to your AI Knowledge Assistant project!

This is the starting point of our app.

We'll slowly turn this into a real RAG-based assistant.

```



If this works:

🎉 \*\*Congrats\*\* — you already have a tiny working app.



---



**### ✅ Step 6: First Commit**



Now tell Git to track these files:



```bash

git add .

git commit -m "Initial setup: project skeleton with app.py and basic files"

```



(If Git asks for your name/email, we can set that up next time.)



---



**### ✅ Step 7: (Optional Today) Create GitHub Repo**



If you still have time in your 1-hour slot:



1\. Go to GitHub → New repository → name: `ai-knowledge-assistant`

2\. Don’t add README (we already have one).

3\. Copy the repo’s URL.

In your terminal:



```bash

git remote add origin <your\_repo\_url>

git branch -M main

git push -u origin main

```



---



**Recall for what we had learned in Day 1**



\* ✅ Project created

\* ✅ Python file runs

\* ✅ Git initialized

\* ✅ First commit done

\* ✅ Code pushed to GitHub



Let me just \*\*lock in the concepts\*\* of what you did today so it’s crystal clear in your mind.



---



\## 🧠 What you did today (Day 1) — in simple English



\### 1️⃣ `git init`



You told Git:



> “From now on, please track this folder as a project.”



Git created a hidden folder: `.git`

That’s where it stores the entire history of your code.



---



\### 2️⃣ You created and ran `app.py`



\* Wrote a small Python program

\* Fixed:



&nbsp; \* Not saving file

&nbsp; \* Indentation

\* Ran it with:



```bash

python src/app.py

```



Python read your code and printed:



```text

👋 Hi Sahi, welcome to your AI Knowledge Assistant project!

...

```



That’s your \*\*entry point\*\* – the “start” of your AI project.



---



\### 3️⃣ `git status`



You checked what Git sees:



```bash

git status

```



Git said something like:



\* `Untracked files:` → “I see these files but haven’t started tracking them.”



This is like Git saying:



> “These things exist, but they’re not in any saved snapshot yet.”



---



\### 4️⃣ `git add .`



You ran:



```bash

git add .

```



This means:



> “Stage all current changes so they’re ready to be saved in a commit.”



Think of it as:



\* \*\*Working folder\*\* → “draft”

\* \*\*Staging area\*\* → “ready for snapshot”

\* \*\*Commit\*\* → “snapshot taken”



`git add .` moves all changes to the staging area.



---



\### 5️⃣ `git commit -m "..."`



You ran:



```bash

git commit -m "Initial setup: project skeleton with app.py and basic files"

```



This means:



> “Take a snapshot of everything staged and save it with this message.”



Now Git permanently remembers:



\* What files existed

\* What they contained at this moment



If you mess up later, you can always go back to this point.



---



\### 6️⃣ `git remote add origin ...`



You added a \*\*link to GitHub\*\*:



```bash

git remote add origin https://github.com/SahithyaGodishala838/ai-knowledge-assistant.git

```



This means:



> “My main remote copy (called `origin`) lives at this GitHub URL.”



So now your local repo knows \*\*where\*\* to push.



---



\### 7️⃣ `git branch -M main`



```bash

git branch -M main

```



Means:



> “Make my current branch called `main`.”



Most modern repos use `main` (instead of `master`).



---



\### 8️⃣ `git push -u origin main`



```bash

git push -u origin main

```



This means:



> “Send my local `main` branch to the `origin` remote on GitHub and link them.”



\* Your code was uploaded

\* GitHub now shows your files

\* `-u` sets tracking, so next time you can just do `git push`.



---



\## ✅ Where you stand now



You now have:



\* A \*\*local project\*\* on your laptop

\* A \*\*remote copy\*\* of the same project on GitHub

\* A \*\*working Python app\*\* you can extend later



This is \*exactly\* how real devs work.



---



\## ⏭️ When you’re ready for Day 2



Just come back and say:



> “Chitti, let’s start Day 2.”



And we’ll:



\* Create `data/documents/`

\* Add your first `.txt` knowledge file

\* Write a loader to read docs with Python

\* Start moving toward embeddings \& RAG



For now, enjoy the win. You absolutely nailed Day 1 💛





