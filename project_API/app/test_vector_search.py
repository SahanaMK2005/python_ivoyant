from app.vector_store import search_vector_db


# -----------------------------------
# CUSTOMER QUESTION
# -----------------------------------

query = "When will I receive my refund?"


# -----------------------------------
# SEARCH CHROMADB
# -----------------------------------

results = search_vector_db(
    query=query,
    n_results=3
)


# -----------------------------------
# PRINT RESULTS
# -----------------------------------

print("\nCustomer Question:")
print(query)

print("\nRetrieved Results:")

for document in results["documents"][0]:

    print(document)