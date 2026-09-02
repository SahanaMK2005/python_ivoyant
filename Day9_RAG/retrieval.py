import chromadb
from sentence_transformers import SentenceTransformer


# ---------------------------------------------------------
# 1. LOAD EMBEDDING MODEL
# ---------------------------------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# ---------------------------------------------------------
# 2. CONNECT TO CHROMADB
# ---------------------------------------------------------

client = chromadb.PersistentClient(
    path="./chroma_db"
)


# ---------------------------------------------------------
# 3. GET COLLECTION
# ---------------------------------------------------------

collection = client.get_collection(
    name="company_handbook"
)


# ---------------------------------------------------------
# 4. USER QUESTION
# ---------------------------------------------------------

question = "What are the working hours?"


# ---------------------------------------------------------
# 5. CREATE QUESTION EMBEDDING
# ---------------------------------------------------------

question_embedding = model.encode(question)


# ---------------------------------------------------------
# 6. SEARCH CHROMADB
# ---------------------------------------------------------

results = collection.query(
    query_embeddings=[question_embedding.tolist()],
    n_results=3
)


# ---------------------------------------------------------
# 7. DISPLAY RESULTS
# ---------------------------------------------------------

print("=" * 60)
print("SEMANTIC SEARCH")
print("=" * 60)

print(f"\nQuestion:")
print(question)

print("\n" + "=" * 60)
print("RETRIEVED CHUNKS")
print("=" * 60)


for index, document in enumerate(results["documents"][0]):

    print(f"\n--- Result {index + 1} ---")

    print(document)

    print("\nChunk ID:")

    print(results["ids"][0][index])

    print("\nDistance:")

    print(results["distances"][0][index])