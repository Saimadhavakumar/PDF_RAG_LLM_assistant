# PDF RAG LLM Assistant

A Retrieval-Augmented Generation (RAG) system that allows users to query PDF documents using a Large Language Model.

## Features
- Upload PDF documents
- Automatic text extraction and chunking
- Embeddings stored in FAISS vector database
- Semantic search to retrieve relevant chunks
- LLM generates accurate answers based on document context

## Architecture
PDF → Chunking → Embeddings → FAISS → Retrieval → Gemini LLM → Answer

## Tech Stack
Python  
FAISS  
Google Gemini API  
PyPDF2  

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Add your Gemini API key in config

3. Run

python main.py

## Example Use Case
Ask questions like:
"What skills does this resume contain?"
"Summarize this document"
