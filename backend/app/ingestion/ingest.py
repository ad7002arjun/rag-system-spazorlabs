from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.utils.file_loader import load_document
from app.rag.vector_store import create_vector_store
from app.config import CHUNK_SIZE, CHUNK_OVERLAP

def ingest_document(file_path: str):
    documents = load_document(file_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)
    create_vector_store(chunks)

    return {"chunks_created": len(chunks)}
