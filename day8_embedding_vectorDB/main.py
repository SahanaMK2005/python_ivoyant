import chromadb

from products import products
from embeddings import generate_embedding


# --------------------------------
# Create ChromaDB client
# --------------------------------

client = chromadb.PersistentClient(
    path="./chroma_db"
)


# --------------------------------
# Create or get product collection
# --------------------------------

collection = client.get_or_create_collection(
    name="products"
)


# --------------------------------
# Store products and embeddings
# --------------------------------

if collection.count() == 0:

    print("Creating product embeddings...\n")

    for index, product in enumerate(products):

        embedding = generate_embedding(product)

        collection.add(
            ids=[str(index + 1)],
            documents=[product],
            embeddings=[embedding]
        )

        print(f"Stored product {index + 1}: {product}")

    print(f"\nTotal products stored: {collection.count()}")


# --------------------------------
# Semantic Search
# --------------------------------

query = input("\nEnter your search query: ")

query_embedding = generate_embedding(query)


# Search ChromaDB
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3,
    include=["documents", "distances"]
)


# --------------------------------
# Check whether the query is relevant
# --------------------------------

best_distance = results["distances"][0][0]

# Internal threshold.
# This value is NOT shown to the user.
THRESHOLD = 0.75


print("\n===== SEMANTIC SEARCH RESULTS =====")

if best_distance > THRESHOLD:

    print("\nNo relevant search found.")

else:

    print("\nTop 3 Similar Products:\n")

    for index, product in enumerate(
        results["documents"][0],
        start=1
    ):
        print(f"{index}. {product}")