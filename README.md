# RAG System – SpazorLabs Assessment

A full-stack **Retrieval-Augmented Generation (RAG)** system built as part of the SpazorLabs technical assessment.  
The project allows users to upload documents and ask questions that are answered using document context via a local LLM.

---

## 🚀 Features

- 📄 Upload documents (TXT, PDF, DOCX)
- 🔍 Vector-based semantic search using FAISS
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Local LLM inference using **Ollama**
- ⚡ FastAPI backend
- 🎨 Clean frontend UI (HTML, CSS, JavaScript)
- 🔒 No cloud dependency (runs fully locally)

---

## 🛠️ Tech Stack

### Backend
- Python 3.11
- FastAPI
- LangChain
- FAISS
- HuggingFace Embeddings
- Ollama (Local LLM)

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

## 📁 Project Structure

```text
rag-system-spazorlabs/
│
├── backend/
│   ├── app/
│   │   ├── ingestion/        # Document ingestion
│   │   ├── rag/              # Embeddings, vector store, QA chain
│   │   ├── utils/            # File loaders
│   │   ├── main.py           # FastAPI entry point
│   │   └── config.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── .gitignore
⚙️ How It Works
User uploads a document

Document is split into chunks

Chunks are converted into embeddings

Embeddings are stored in FAISS vector DB

User asks a question

Relevant document chunks are retrieved

Local LLM generates an answer using retrieved context

▶️ Running the Project Locally
1️⃣ Start Ollama

ollama run llama3
2️⃣ Start Backend

cd backend
uvicorn app.main:app --reload
Backend will run at:

http://127.0.0.1:8000
3️⃣ Open Frontend
Simply open:


frontend/index.html
in your browser
(or use Live Server in VS Code)

🧪 API Endpoints
Upload Document

POST /upload
Ask Question

POST /ask
Request body:

json

{
  "question": "What does SpazorLabs do?"
}
🌐 Live Demo
Local deployment (runs fully offline using Ollama)

📦 Repository
GitHub Repo:
👉 https://github.com/ad7002arjun/rag-system-spazorlabs

🧑‍💻 Author
Arjun Dogra
GitHub: https://github.com/ad7002arjun

