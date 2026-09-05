from pypdf import PdfReader
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
# 2. FIXED-SIZE CHUNKING
# ---------------------------------------------------------
def fixed_size_chunking(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


# ---------------------------------------------------------
# 3. RECURSIVE CHUNKING
# ---------------------------------------------------------
def recursive_chunking(text, chunk_size=500, overlap=50):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,

        separators=[
            "\n\n",   # Paragraph
            "\n",     # New line
            ". ",     # Sentence
            " ",      # Word
            ""        # Character
        ]
    )

    chunks = splitter.split_text(text)

    return chunks


# ---------------------------------------------------------
# 4. MAIN PROGRAM
# ---------------------------------------------------------
if __name__ == "__main__":

    # PDF location
    pdf_path = "documents/company_handbook.pdf"

    # -----------------------------------------------------
    # Load PDF
    # -----------------------------------------------------
    text = load_pdf(pdf_path)

    # -----------------------------------------------------
    # Fixed-size chunking
    # -----------------------------------------------------
    fixed_chunks = fixed_size_chunking(
        text,
        chunk_size=500
    )

    # -----------------------------------------------------
    # Recursive chunking
    # -----------------------------------------------------
    recursive_chunks = recursive_chunking(
        text,
        chunk_size=500,
        overlap=50
    )

    # -----------------------------------------------------
    # PDF INFORMATION
    # -----------------------------------------------------
    print("=" * 60)
    print("PDF INFORMATION")
    print("=" * 60)

    print(f"Total characters: {len(text)}")

    # -----------------------------------------------------
    # Fixed-size information
    # -----------------------------------------------------
    print("\n" + "=" * 60)
    print("FIXED-SIZE CHUNKING")
    print("=" * 60)

    print(f"Total fixed-size chunks: {len(fixed_chunks)}")

    # -----------------------------------------------------
    # Display fixed-size chunks
    # -----------------------------------------------------
    for index, chunk in enumerate(fixed_chunks):

        print(f"\n--- Fixed Chunk {index + 1} ---")

        print(chunk)

    # -----------------------------------------------------
    # Recursive information
    # -----------------------------------------------------
    print("\n" + "=" * 60)
    print("RECURSIVE CHUNKING")
    print("=" * 60)

    print(f"Total recursive chunks: {len(recursive_chunks)}")

    # -----------------------------------------------------
    # Display recursive chunks
    # -----------------------------------------------------
    for index, chunk in enumerate(recursive_chunks):

        print(f"\n--- Recursive Chunk {index + 1} ---")

        print(chunk)