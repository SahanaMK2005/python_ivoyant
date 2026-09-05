import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)
from langchain_chroma import Chroma


# ==========================================
# Configuration
# ==========================================

PDF_PATH = "data/Python_Programming_Guide.pdf"
CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "python_guide"


# ==========================================
# Step 1: Load PDF
# ==========================================

def load_pdf():
    """Load the PDF and return LangChain documents."""

    loader = PyPDFLoader(PDF_PATH)

    documents = loader.load()

    return documents


# ==========================================
# Step 2: Split documents into chunks
# ==========================================

def split_documents(documents):
    """Split documents into smaller chunks for RAG."""

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


# ==========================================
# Step 3: Create Gemini embedding model
# ==========================================

def create_embeddings():
    """Create the Gemini embedding model."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not set."
        )

    print("Gemini API key loaded:", True)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=api_key
    )

    return embeddings


# ==========================================
# Step 4: Create ChromaDB vector store
# ==========================================

def create_vector_store(chunks, embeddings):
    """Create ChromaDB if it does not exist, otherwise load it."""

    # Check whether ChromaDB already exists
    if os.path.exists(CHROMA_PATH) and os.listdir(CHROMA_PATH):

        print("Existing ChromaDB found. Loading it...")

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embeddings,
            persist_directory=CHROMA_PATH
        )

        print("Existing ChromaDB loaded.")

    else:

        print("No existing ChromaDB found. Creating new database...")

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_PATH,
            collection_name=COLLECTION_NAME
        )

        print("New ChromaDB created.")

    return vector_store
# ==========================================
# Step 5: Search relevant documents
# ==========================================

def search_documents(vector_store, query):
    """Retrieve the top 3 relevant document chunks."""

    results = vector_store.similarity_search(
        query,
        k=3
    )

    return results


# ==========================================
# Step 6: Create Gemini chat model
# ==========================================

def create_llm():
    """Create the Gemini LLM used for answer generation."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not set."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        google_api_key=api_key
    )

    return llm


# ==========================================
# Step 7: Generate answer using RAG
# ==========================================

def generate_answer(llm, query, documents):
    """Generate an answer using retrieved document context."""

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
You are a helpful Python programming assistant.

Answer the user's question using only the information
provided in the context below.

If the answer is not available in the context,
say that the information is not available in the document.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    # Handle normal string response
    if isinstance(response.content, str):
        return response.content

    # Handle structured Gemini response
    if isinstance(response.content, list):

        for item in response.content:

            if (
                isinstance(item, dict)
                and item.get("type") == "text"
            ):
                return item.get("text", "")

    return str(response.content)


# ==========================================
# Main RAG Pipeline
# ==========================================

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("STARTING LANGCHAIN RAG PIPELINE")
    print("=" * 60)

    try:

        # --------------------------------------
        # 1. Load PDF
        # --------------------------------------

        documents = load_pdf()

        print(
            f"\nTotal pages loaded: {len(documents)}"
        )

        # --------------------------------------
        # 2. Split documents
        # --------------------------------------

        chunks = split_documents(documents)

        print(
            f"Total chunks created: {len(chunks)}"
        )

        # --------------------------------------
        # 3. Create embeddings
        # --------------------------------------

        embeddings = create_embeddings()

        print("Embedding model created successfully.")

        # --------------------------------------
        # 4. Create ChromaDB
        # --------------------------------------

        vector_store = create_vector_store(
            chunks,
            embeddings
        )

        print(
            "Documents successfully stored in ChromaDB."
        )

        # --------------------------------------
        # 5. User question
        # --------------------------------------

        query = "What is a Python variable?"

        print(
            f"\nUser Question: {query}"
        )

        # --------------------------------------
        # 6. Retrieve relevant chunks
        # --------------------------------------

        results = search_documents(
            vector_store,
            query
        )

        print(
            "\nRetrieved Documents:"
        )

        for i, result in enumerate(results):

            print("\n" + "=" * 60)
            print(f"Result {i + 1}")
            print("=" * 60)

            print(result.page_content)

            print(
                f"\nPage: {result.metadata.get('page')}"
            )

        # --------------------------------------
        # 7. Create Gemini LLM
        # --------------------------------------

        llm = create_llm()

        print(
            "\nGemini chat model created successfully."
        )

        # --------------------------------------
        # 8. Generate final answer
        # --------------------------------------

        answer = generate_answer(
            llm,
            query,
            results
        )

        print("\n" + "=" * 60)
        print("FINAL ANSWER")
        print("=" * 60)

        print(answer)

    except Exception as e:

        print("\n" + "=" * 60)
        print("ERROR")
        print("=" * 60)

        print(f"{type(e).__name__}: {e}")
