from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb


# ---------------------------------------------------------
# 1. LOAD PDF
# ---------------------------------------------------------
def load_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ---------------------------------------------------------
# 2. RECURSIVE CHUNKING
# ---------------------------------------------------------
def recursive_chunking(text, chunk_size=500, overlap=50):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_text(text)

    return chunks


# ---------------------------------------------------------
# 3. MAIN PROGRAM
# ---------------------------------------------------------
if __name__ == "__main__":

    # -----------------------------------------------------
    # PDF PATH
    # -----------------------------------------------------

    pdf_path = "documents/company_handbook.pdf"

    # -----------------------------------------------------
    # LOAD PDF
    # -----------------------------------------------------

    print("=" * 60)
    print("LOADING PDF")
    print("=" * 60)

    text = load_pdf(pdf_path)

    print(f"Total characters: {len(text)}")

    # -----------------------------------------------------
    # CREATE CHUNKS
    # -----------------------------------------------------

    chunks = recursive_chunking(
        text,
        chunk_size=500,
        overlap=50
    )

    print(f"Total chunks: {len(chunks)}")

    # -----------------------------------------------------
    # LOAD EMBEDDING MODEL
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("LOADING EMBEDDING MODEL")
    print("=" * 60)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Embedding model loaded.")

    # -----------------------------------------------------
    # CREATE EMBEDDINGS
    # -----------------------------------------------------

    print("\nCreating embeddings...")

    embeddings = model.encode(chunks)

    print("Embeddings created.")

    # -----------------------------------------------------
    # CREATE CHROMADB CLIENT
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("INITIALIZING CHROMADB")
    print("=" * 60)

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    print("ChromaDB initialized.")

    # -----------------------------------------------------
    # CREATE COLLECTION
    # -----------------------------------------------------

    collection = client.get_or_create_collection(
        name="company_handbook"
    )

    print("Collection created/loaded.")

    # -----------------------------------------------------
    # CREATE IDS
    # -----------------------------------------------------

    ids = []

    for index in range(len(chunks)):

        ids.append(f"chunk_{index + 1}")

    # -----------------------------------------------------
    # CREATE METADATA
    # -----------------------------------------------------

    metadatas = []

    for index in range(len(chunks)):

        metadatas.append({
            "source": "company_handbook.pdf",
            "chunk_number": index + 1
        })

    # -----------------------------------------------------
    # STORE DATA IN CHROMADB
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("STORING DATA IN CHROMADB")
    print("=" * 60)

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

    # -----------------------------------------------------
    # VERIFY DATABASE
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("CHROMADB VERIFICATION")
    print("=" * 60)

    result = collection.get()

    print(f"Total records in collection: {len(result['ids'])}")

    print("\nStored IDs:")

    print(result["ids"])