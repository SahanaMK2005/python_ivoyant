# AI-Powered Customer Support System

This project is an AI-powered customer support system built using FastAPI and Streamlit.

The system uses a RAG pipeline to answer customer questions based on company policies.

Customer questions are converted into embeddings and searched in ChromaDB using semantic similarity.

The relevant knowledge is retrieved and provided to the Gemini LLM to generate an AI response.

The project also includes a Knowledge Management module to view and update company policies.

Knowledge is stored persistently in `data/knowledge.json`.

APScheduler automatically synchronizes updated knowledge with ChromaDB every 1 minute.

## Technologies Used

FastAPI, Streamlit, ChromaDB, Sentence Transformers, Gemini LLM, LangChain, APScheduler, and Python.