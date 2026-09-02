import os
import chromadb
from sentence_transformers import SentenceTransformer
from google import genai


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_collection(
    name="company_handbook"
)


# Connect to Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set."
    )

gemini_client = genai.Client(
    api_key=api_key
)


def ask_question(question):

    question_embedding = model.encode(question)

    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a company handbook assistant.

Answer the user's question using only the provided context.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided company handbook."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text, retrieved_chunks