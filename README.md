# PDF RAG LLM Assistant

A Retrieval-Augmented Generation (RAG) based application that allows users to upload PDF documents and ask questions about their content using a Large Language Model (LLM). The system uses vector embeddings and semantic search to retrieve relevant document sections and generate accurate, context-aware answers.

This project demonstrates real-world GenAI engineering concepts including embeddings, vector databases, semantic retrieval, and LLM integration.

---

## Features

- Load and process PDF documents
- Automatic text extraction and intelligent chunking
- Generate embeddings for document chunks
- Store embeddings in FAISS vector database
- Semantic similarity search for relevant content
- Accurate answers generated using Google Gemini LLM
- Modular and scalable backend architecture

---

## Architecture

PDF Document  
↓  
Text Extraction (PyPDF2)  
↓  
Text Chunking  
↓  
Embedding Generation  
↓  
FAISS Vector Database  
↓  
User Question  
↓  
Semantic Retrieval  
↓  
Gemini LLM  
↓  
Final Answer  

---

## Tech Stack

Language:
- Python

GenAI / LLM:
- Google Gemini API

Vector Database:
- FAISS (Facebook AI Similarity Search)

Libraries:
- PyPDF2  
- NumPy  
- python-dotenv  

---

## Project Structure

PDF_RAG_LLM_assistant/

main.py              # Entry point of the application  
rag_agent.py        # Handles retrieval and LLM interaction  
embeddings.py       # Embedding creation and vector storage  
pdf_loader.py       # PDF loading and text extraction  
config.py           # API configuration  
requirements.txt    # Project dependencies  
README.md  

---

## How It Works

1. User provides a PDF document  
2. System extracts text and splits it into smaller chunks  
3. Each chunk is converted into vector embeddings  
4. Embeddings are stored in FAISS vector database  
5. User asks a question  
6. System retrieves the most relevant chunks using semantic similarity search  
7. Retrieved context is passed to the Gemini LLM  
8. LLM generates a context-aware answer  

---

## Installation

Clone the repository:

git clone https://github.com/Saimadhavakumar/PDF_RAG_LLM_assistant.git  
cd PDF_RAG_LLM_assistant  

Install dependencies:

pip install -r requirements.txt  

---

## Configuration

Add your Google Gemini API key in config.py:

GEMINI_API_KEY = "your_api_key_here"

---

## Run the Application

python main.py

---

## Example Questions

- What skills are mentioned in this resume?  
- Summarize this document  
- What is the main topic of this PDF?  
- Explain the key points in simple terms  

---

## Use Cases

- Resume analysis assistant  
- Research paper question answering  
- Study material assistant  
- Enterprise document search  
- Knowledge base assistant  

---

## Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)  
- Vector embeddings  
- Semantic similarity search  
- Vector databases (FAISS)  
- LLM integration with external knowledge  
- Context grounding to reduce hallucinations  

---

## Future Improvements

- Add web interface (Streamlit or React)  
- Support multiple PDF uploads  
- Persistent vector database storage  
- Docker containerization  
- Cloud deployment (AWS / Azure / GCP)  

---

## Author

Sai Madhava  
GitHub: https://github.com/Saimadhavakumar  

---

## License

This project is for educational and demonstration purposes.
