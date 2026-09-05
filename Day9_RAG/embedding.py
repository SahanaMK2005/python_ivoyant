from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


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

    # PDF path
    pdf_path = "documents/company_handbook.pdf"

    # Load PDF
    text = load_pdf(pdf_path)

    print("=" * 60)
    print("PDF INFORMATION")
    print("=" * 60)

    print(f"Total characters: {len(text)}")

    # Create recursive chunks
    chunks = recursive_chunking(
        text,
        chunk_size=500,
        overlap=50
    )

    print(f"Total chunks: {len(chunks)}")

    # -----------------------------------------------------
    # 4. LOAD EMBEDDING MODEL
    # -----------------------------------------------------

    print("\nLoading embedding model...")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Embedding model loaded successfully.")

    # -----------------------------------------------------
    # 5. CREATE EMBEDDINGS
    # -----------------------------------------------------

    print("\nCreating embeddings...")

    embeddings = model.encode(chunks)

    print("Embeddings created successfully.")

    # -----------------------------------------------------
    # 6. DISPLAY INFORMATION
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("EMBEDDING INFORMATION")
    print("=" * 60)

    print(f"Number of chunks: {len(chunks)}")

    print(f"Number of embeddings: {len(embeddings)}")

    print(f"Embedding dimensions: {len(embeddings[0])}")

    # -----------------------------------------------------
    # 7. DISPLAY FIRST FEW CHUNKS
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("SAMPLE CHUNKS AND EMBEDDINGS")
    print("=" * 60)

    for index in range(min(3, len(chunks))):

        print(f"\n--- Chunk {index + 1} ---")

        print(chunks[index])

        print("\nEmbedding preview:")

        print(embeddings[index][:10])

        print(f"Vector dimensions: {len(embeddings[index])}")