import pickle
import faiss
import numpy as np
from google import genai
from config import GOOGLE_API_KEY, EMBEDDING_MODEL, FAISS_INDEX_PATH

client = genai.Client(api_key=GOOGLE_API_KEY)

def embed_text(text: str) -> list:
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )
    # IMPORTANT: extract actual vector
    return response.embeddings[0].values


def create_faiss_index(chunks):
    vectors = [embed_text(chunk) for chunk in chunks]
    vectors = np.array(vectors).astype("float32")

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    with open(FAISS_INDEX_PATH, "wb") as f:
        pickle.dump((index, chunks), f)

    return index, chunks


def load_faiss_index():
    with open(FAISS_INDEX_PATH, "rb") as f:
        return pickle.load(f)
