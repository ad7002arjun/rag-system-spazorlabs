from fastapi import FastAPI, UploadFile, File
from app.ingestion.ingest import ingest_document
from app.rag.qa_chain import get_qa_chain
from app.schemas import QueryRequest
import shutil
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="RAG System - SpazorLabs")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

qa_chain = None

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    result = ingest_document(file_path)
    return result

@app.post("/ask")
def ask_question(query: QueryRequest):
    global qa_chain
    if qa_chain is None:
        qa_chain = get_qa_chain()

    result = qa_chain.invoke(query.question)
    return {"answer": result.content}


