import os
from pdf_loader import load_pdf_text, chunk_text
from embeddings import create_faiss_index
from rag_agent import query_faiss, ask_llm
from config import PDF_PATH, FAISS_INDEX_PATH

def main():
    if not os.path.exists(FAISS_INDEX_PATH):
        print("Reading PDF...")
        text = load_pdf_text(PDF_PATH)
        chunks = chunk_text(text)
        print(f"Total chunks: {len(chunks)}")
        print("Creating embeddings & FAISS index...")
        create_faiss_index(chunks)
    else:
        print("Loading existing FAISS index...")

    while True:
        query = input("\nAsk a question (or type exit): ")
        if query.lower() == "exit":
            break

        try:
            context = query_faiss(query)
            answer = ask_llm(query, context)
            print("\nAnswer:\n", answer)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
