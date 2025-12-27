import numpy as np
from google import genai
from embeddings import embed_text, load_faiss_index
from config import GOOGLE_API_KEY, LLM_MODEL

client = genai.Client(api_key=GOOGLE_API_KEY)

def query_faiss(query, top_k=3):
    index, chunks = load_faiss_index()

    query_vector = np.array([embed_text(query)]).astype("float32")
    distances, indices = index.search(query_vector, top_k)

    return [chunks[i] for i in indices[0]]


def ask_llm(query, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an expert DevOps instructor.

Answer the question using ONLY the information from the context below.
Give a COMPLETE, DETAILED, and WELL-STRUCTURED explanation.
If the answer has multiple steps or phases, explain EACH one clearly.
Do not cut the answer midway.

Context:
{context}

Question:
{query}

Answer (detailed):
"""

    response = client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt,
    )

    return response.text
