from langchain_google_genai import ChatGoogleGenerativeAI

from app.vector_store import search_vector_db


# -----------------------------------
# INITIALIZE GEMINI MODEL
# -----------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0
)


# -----------------------------------
# GENERATE RAG ANSWER
# -----------------------------------

def generate_rag_answer(question: str):


    # -----------------------------------
    # STEP 1: SEARCH VECTOR DATABASE
    # -----------------------------------

    results = search_vector_db(
        query=question,
        n_results=3
    )


    documents = results["documents"][0]


    # -----------------------------------
    # STEP 2: CHECK RESULTS
    # -----------------------------------

    if not documents:

        return {
            "answer": "Sorry, I could not find relevant information.",
            "retrieved_knowledge": []
        }


    # -----------------------------------
    # STEP 3: CREATE CONTEXT
    # -----------------------------------

    context = "\n\n".join(documents)


    # -----------------------------------
    # STEP 4: CREATE PROMPT
    # -----------------------------------

    prompt = f"""
You are an AI customer support assistant for an e-commerce company.

Answer the customer's question using ONLY the provided company knowledge.

If the answer is not available in the provided knowledge, say:

"I could not find this information in the company knowledge."

Company Knowledge:

{context}

Customer Question:

{question}

Provide a clear, helpful, and concise answer.
"""


    # -----------------------------------
    # STEP 5: CALL GEMINI
    # -----------------------------------

    response = llm.invoke(prompt)

    # -----------------------------------
    # STEP 6: GET TEXT RESPONSE
    # -----------------------------------

    answer = response.content

    if isinstance(answer, list):
        answer = answer[0]["text"]

    # -----------------------------------
    # STEP 7: RETURN ANSWER
    # -----------------------------------

    return {
        "answer": answer,
        "retrieved_knowledge": documents
    }