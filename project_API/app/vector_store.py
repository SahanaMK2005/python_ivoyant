import chromadb
from sentence_transformers import SentenceTransformer


# -----------------------------------
# EMBEDDING MODEL
# -----------------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# -----------------------------------
# CHROMADB CLIENT
# -----------------------------------

client = chromadb.PersistentClient(
    path="chroma_db"
)


# -----------------------------------
# CREATE / GET COLLECTION
# -----------------------------------

collection = client.get_or_create_collection(
    name="customer_support_knowledge"
)


# -----------------------------------
# CREATE EMBEDDING
# -----------------------------------

def create_embedding(text):

    embedding = embedding_model.encode(text)

    return embedding.tolist()


# -----------------------------------
# STORE KNOWLEDGE IN CHROMADB
# -----------------------------------

def add_knowledge_to_vector_db(
    knowledge_id,
    category,
    content
):

    # Combine category and content

    text = f"{category}: {content}"


    # Create embedding

    embedding = create_embedding(text)


    # Add data to ChromaDB

    collection.upsert(

        ids=[str(knowledge_id)],

        embeddings=[embedding],

        documents=[text],

        metadatas=[

            {
                "category": category,
                "content": content
            }

        ]

    )


# -----------------------------------
# SEARCH KNOWLEDGE
# -----------------------------------

def search_vector_db(query, n_results=3):

    query_embedding = create_embedding(query)


    results = collection.query(

        query_embeddings=[
            query_embedding
        ],

        n_results=n_results

    )


    return results