from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from app.schemas import (
    KnowledgeCreate,
    KnowledgeUpdate,
    KnowledgePatch
)

from app.vector_store import search_vector_db
from app.rag_service import generate_rag_answer
from app.scheduler_service import start_scheduler

import json
import os


# -----------------------------------
# FILE PATH CONFIGURATION
# -----------------------------------

# Get project_API folder path
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Data folder path
DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

# Knowledge JSON file path
DATA_FILE = os.path.join(
    DATA_DIR,
    "knowledge.json"
)


# Print exact file path
print("Knowledge file path:", DATA_FILE)


# -----------------------------------
# CREATE DATA FOLDER IF NOT EXISTS
# -----------------------------------

if not os.path.exists(DATA_DIR):

    os.makedirs(DATA_DIR)


# -----------------------------------
# CREATE DATA FILE IF NOT EXISTS
# -----------------------------------

if not os.path.exists(DATA_FILE):

    with open(DATA_FILE, "w") as file:

        json.dump([], file, indent=4)


# -----------------------------------
# FASTAPI LIFESPAN
# -----------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Start scheduler automatically
    start_scheduler(interval_minutes=1)

    print("Scheduler started automatically!")

    yield


# -----------------------------------
# FASTAPI APPLICATION
# -----------------------------------

app = FastAPI(

    title="AI-Powered E-Commerce Customer Support API",

    lifespan=lifespan

)


# -----------------------------------
# READ KNOWLEDGE DATA
# -----------------------------------

def load_knowledge():

    with open(DATA_FILE, "r") as file:

        return json.load(file)


# -----------------------------------
# SAVE KNOWLEDGE DATA
# -----------------------------------

def save_knowledge(data):

    with open(DATA_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


# -----------------------------------
# HOME API
# -----------------------------------

@app.get("/")
def home():

    return {

        "message": "AI-Powered E-Commerce Customer Support API"

    }


# -----------------------------------
# HEALTH CHECK
# -----------------------------------

@app.get("/health")
def health_check():

    return {

        "status": "API is running successfully"

    }


# -----------------------------------
# CREATE KNOWLEDGE
# -----------------------------------

@app.post("/knowledge")
def create_knowledge(knowledge: KnowledgeCreate):

    knowledge_base = load_knowledge()


    # Generate new ID

    if len(knowledge_base) == 0:

        new_id = 1

    else:

        new_id = max(

            item["id"]

            for item in knowledge_base

        ) + 1


    # Create new knowledge

    new_knowledge = {

        "id": new_id,

        "category": knowledge.category,

        "content": knowledge.content

    }


    # Add knowledge

    knowledge_base.append(
        new_knowledge
    )


    # Save knowledge

    save_knowledge(
        knowledge_base
    )


    return {

        "message": "Knowledge created successfully",

        "data": new_knowledge

    }


# -----------------------------------
# GET ALL KNOWLEDGE
# -----------------------------------

@app.get("/knowledge")
def get_all_knowledge():

    knowledge_base = load_knowledge()


    return {

        "total": len(knowledge_base),

        "data": knowledge_base

    }


# -----------------------------------
# KEYWORD SEARCH KNOWLEDGE
# -----------------------------------

@app.get("/knowledge/search")
def search_knowledge(query: str):

    knowledge_base = load_knowledge()

    results = []


    for knowledge in knowledge_base:

        if (

            query.lower()
            in knowledge["category"].lower()

            or

            query.lower()
            in knowledge["content"].lower()

        ):

            results.append(
                knowledge
            )


    return {

        "query": query,

        "total": len(results),

        "data": results

    }


# -----------------------------------
# SEMANTIC SEARCH KNOWLEDGE
# -----------------------------------

@app.get("/knowledge/semantic-search")
def semantic_search(query: str):


    results = search_vector_db(

        query=query,

        n_results=3

    )


    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    ids = results["ids"][0]


    search_results = []


    for i in range(

        len(documents)

    ):


        search_results.append({

            "id": ids[i],

            "category": metadatas[i]["category"],

            "content": metadatas[i]["content"]

        })


    return {

        "query": query,

        "total": len(search_results),

        "data": search_results

    }


# -----------------------------------
# GET KNOWLEDGE BY ID
# -----------------------------------

@app.get("/knowledge/{knowledge_id}")
def get_knowledge_by_id(

    knowledge_id: int

):


    knowledge_base = load_knowledge()


    for knowledge in knowledge_base:


        if knowledge["id"] == knowledge_id:


            return {

                "data": knowledge

            }


    raise HTTPException(

        status_code=404,

        detail="Knowledge not found"

    )


# -----------------------------------
# FULL UPDATE KNOWLEDGE
# -----------------------------------

@app.put("/knowledge/{knowledge_id}")
def update_knowledge(

    knowledge_id: int,

    knowledge: KnowledgeUpdate

):


    knowledge_base = load_knowledge()


    for item in knowledge_base:


        if item["id"] == knowledge_id:


            # Update category

            item["category"] = (
                knowledge.category
            )


            # Update content

            item["content"] = (
                knowledge.content
            )


            # Save updated knowledge

            save_knowledge(

                knowledge_base

            )


            return {

                "message":
                    "Knowledge updated successfully",

                "data": item

            }


    raise HTTPException(

        status_code=404,

        detail="Knowledge not found"

    )


# -----------------------------------
# PARTIAL UPDATE KNOWLEDGE
# -----------------------------------

@app.patch("/knowledge/{knowledge_id}")
def patch_knowledge(

    knowledge_id: int,

    knowledge: KnowledgePatch

):


    knowledge_base = load_knowledge()


    for item in knowledge_base:


        if item["id"] == knowledge_id:


            # Update category

            if knowledge.category is not None:


                item["category"] = (

                    knowledge.category

                )


            # Update content

            if knowledge.content is not None:


                item["content"] = (

                    knowledge.content

                )


            # Save updated knowledge

            save_knowledge(

                knowledge_base

            )


            return {

                "message":
                    "Knowledge updated successfully",

                "data": item

            }


    raise HTTPException(

        status_code=404,

        detail="Knowledge not found"

    )


# -----------------------------------
# DELETE KNOWLEDGE
# -----------------------------------

@app.delete("/knowledge/{knowledge_id}")
def delete_knowledge(

    knowledge_id: int

):


    knowledge_base = load_knowledge()


    for knowledge in knowledge_base:


        if knowledge["id"] == knowledge_id:


            # Remove knowledge

            knowledge_base.remove(

                knowledge

            )


            # Save knowledge

            save_knowledge(

                knowledge_base

            )


            return {

                "message":
                    "Knowledge deleted successfully"

            }


    raise HTTPException(

        status_code=404,

        detail="Knowledge not found"

    )


# -----------------------------------
# AI CUSTOMER SUPPORT - RAG
# -----------------------------------

@app.get("/ask")
def ask_question(

    question: str

):


    # Generate answer using RAG

    result = generate_rag_answer(

        question

    )


    return {

        "question": question,

        "answer": result["answer"],

        "retrieved_knowledge":

            result["retrieved_knowledge"]

    }