import streamlit as st
from rag_pipeline import ask_question


st.set_page_config(
    page_title="Company Handbook AI",
    page_icon="📚",
    layout="centered"
)


st.title("📚 Company Handbook AI")

st.write(
    "Ask questions about the company handbook."
)


question = st.text_input(
    "Enter your question:"
)


if st.button("🔍 Ask Question"):

    if question.strip():

        answer, retrieved_chunks = ask_question(question)

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Retrieved Sources")

        for index, chunk in enumerate(retrieved_chunks):

            with st.expander(
                f"Chunk {index + 1}"
            ):
                st.write(chunk)

    else:

        st.warning(
            "Please enter a question."
        )