import json

from app.vector_store import add_knowledge_to_vector_db


# -----------------------------------
# FILE PATH
# -----------------------------------

DATA_FILE = "data/knowledge.json"


# -----------------------------------
# LOAD JSON DATA
# -----------------------------------

with open(DATA_FILE, "r") as file:

    knowledge_base = json.load(file)


# -----------------------------------
# STORE DATA IN CHROMADB
# -----------------------------------

for knowledge in knowledge_base:

    add_knowledge_to_vector_db(

        knowledge_id=knowledge["id"],

        category=knowledge["category"],

        content=knowledge["content"]

    )

    print(
        f"Stored ID {knowledge['id']} in ChromaDB"
    )


print("All knowledge stored successfully!")