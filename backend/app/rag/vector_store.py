from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embedding_model
from app.config import VECTOR_DB_PATH

def create_vector_store(docs):
    embeddings = get_embedding_model()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(VECTOR_DB_PATH)
    return db

def load_vector_store():
    embeddings = get_embedding_model()
    return FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True  # YOU CREATED IT, SO SAFE
    )


