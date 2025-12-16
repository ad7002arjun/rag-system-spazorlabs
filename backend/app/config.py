import os
from dotenv import load_dotenv
load_dotenv()
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTOR_DB_PATH = "vector_store"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
