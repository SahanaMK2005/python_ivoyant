from app.rag_service import generate_rag_answer


# -----------------------------------
# CUSTOMER QUESTION
# -----------------------------------

question = "When will I receive my refund?"


# -----------------------------------
# GENERATE RAG ANSWER
# -----------------------------------

result = generate_rag_answer(question)


# -----------------------------------
# PRINT QUESTION
# -----------------------------------

print("\nCustomer Question:")

print(question)


# -----------------------------------
# PRINT AI ANSWER
# -----------------------------------

print("\nAI Answer:")

print(result["answer"])


# -----------------------------------
# PRINT RETRIEVED KNOWLEDGE
# -----------------------------------

print("\nRetrieved Knowledge:")


for document in result["retrieved_knowledge"]:

    print(document)