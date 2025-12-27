import os

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

EMBEDDING_MODEL = "models/text-embedding-004"
LLM_MODEL = "models/gemini-2.5-flash"


FAISS_INDEX_PATH = "embeddings/faiss_index.pkl"
PDF_PATH = "UNIT-3 DEVOPS.pdf"
