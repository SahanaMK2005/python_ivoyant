import os
import hashlib

import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from rag_pipeline import (
    create_embeddings,
    search_documents,
    create_llm,
    generate_answer
)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Python Notes AI Assistant",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# Title
# ==========================================

st.title("🤖 Notes AI Assistant")

st.write(
    "Upload a Python PDF and ask questions using LangChain RAG."
)


# ==========================================
# Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_file_hash" not in st.session_state:
    st.session_state.current_file_hash = None


# ==========================================
# Sidebar
# ==========================================

st.sidebar.header("📄 Document")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


# ==========================================
# Clear Chat
# ==========================================

if st.sidebar.button("🧹 Clear Chat"):

    st.session_state.messages = []

    st.rerun()


# ==========================================
# Process Uploaded PDF
# ==========================================

if uploaded_file is not None:

    # --------------------------------------
    # Generate unique file hash
    # --------------------------------------

    file_bytes = uploaded_file.getvalue()

    file_hash = hashlib.md5(
        file_bytes
    ).hexdigest()[:12]


    # --------------------------------------
    # Clear old chat when a new PDF is uploaded
    # --------------------------------------

    if (
        st.session_state.current_file_hash
        != file_hash
    ):

        st.session_state.messages = []

        st.session_state.current_file_hash = (
            file_hash
        )


    # --------------------------------------
    # Save uploaded PDF
    # --------------------------------------

    upload_directory = "data/uploads"

    os.makedirs(
        upload_directory,
        exist_ok=True
    )

    pdf_path = os.path.join(
        upload_directory,
        f"{file_hash}_{uploaded_file.name}"
    )


    if not os.path.exists(pdf_path):

        with open(pdf_path, "wb") as file:

            file.write(file_bytes)


    # --------------------------------------
    # Unique Chroma collection
    # --------------------------------------

    collection_name = (
        f"python_{file_hash}"
    )


    # ======================================
    # Load PDF
    # ======================================

    @st.cache_resource(
        show_spinner="📄 Loading PDF..."
    )
    def load_uploaded_pdf(path):

        loader = PyPDFLoader(path)

        documents = loader.load()

        return documents


    documents = load_uploaded_pdf(
        pdf_path
    )


    # ======================================
    # Split PDF into Chunks
    # ======================================

    @st.cache_resource(
        show_spinner="✂️ Creating document chunks..."
    )
    def create_chunks(path):

        loader = PyPDFLoader(path)

        documents = loader.load()

        text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )
        )

        chunks = text_splitter.split_documents(
            documents
        )

        return chunks


    chunks = create_chunks(
        pdf_path
    )


    # ======================================
    # Create Embeddings
    # ======================================

    @st.cache_resource(
        show_spinner="🧠 Loading Gemini embeddings..."
    )
    def get_embeddings():

        return create_embeddings()


    embeddings = get_embeddings()


    # ======================================
    # Create / Load ChromaDB
    # ======================================

    def get_vector_store(
        chunks,
        embeddings,
        collection_name
    ):
        """Create or load a persistent ChromaDB collection."""

        vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=embeddings,
            persist_directory="chroma_db"
        )


        # Check existing documents

        existing_count = (
            vector_store._collection.count()
        )


        if existing_count == 0:

            with st.spinner(
                "🗄️ Adding documents to ChromaDB..."
            ):

                vector_store.add_documents(
                    chunks
                )

        else:

            print(
                f"Existing ChromaDB found with "
                f"{existing_count} documents."
            )


        return vector_store


    vector_store = get_vector_store(
        chunks,
        embeddings,
        collection_name
    )


    # ======================================
    # Create Gemini LLM
    # ======================================

    @st.cache_resource(
        show_spinner="🤖 Loading Gemini..."
    )
    def get_llm():

        return create_llm()


    llm = get_llm()


    # ======================================
    # Document Statistics
    # ======================================

    st.sidebar.divider()

    st.sidebar.subheader(
        "📊 Document Statistics"
    )

    st.sidebar.write(
        f"**File:** {uploaded_file.name}"
    )

    st.sidebar.write(
        f"**Pages:** {len(documents)}"
    )

    st.sidebar.write(
        f"**Chunks:** {len(chunks)}"
    )

    st.sidebar.write(
        "**Vector Database:** ChromaDB"
    )

    st.sidebar.write(
        "**Embeddings:** Gemini"
    )

    st.sidebar.write(
        "**LLM:** Gemini 3.5 Flash"
    )


    # ======================================
    # Chat History
    # ======================================

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )


            # ----------------------------------
            # Retrieved Context
            # ----------------------------------

            if (
                message["role"] == "assistant"
                and "context" in message
            ):

                with st.expander(
                    "🔎 View Retrieved Context"
                ):

                    for i, document in enumerate(
                        message["context"]
                    ):

                        page_number = (
                            document.metadata.get(
                                "page",
                                "Unknown"
                            )
                        )

                        st.markdown(
                            f"**Result {i + 1} "
                            f"— Page {page_number}**"
                        )

                        st.write(
                            document.page_content
                        )

                        st.divider()


    # ======================================
    # Chat Input
    # ======================================

    user_question = st.chat_input(
        "Ask a new question about the PDF..."
    )


    # ======================================
    # Process Question
    # ======================================

    if user_question:

        # ----------------------------------
        # Display User Question
        # ----------------------------------

        with st.chat_message("user"):

            st.markdown(
                user_question
            )


        # Save user message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )


        # ----------------------------------
        # Retrieve Relevant Documents
        # ----------------------------------

        with st.spinner(
            "🔎 Searching the document..."
        ):

            results = search_documents(
                vector_store,
                user_question
            )


        # ----------------------------------
        # Generate Answer
        # ----------------------------------

        with st.spinner(
            "🤖 Generating answer..."
        ):

            answer = generate_answer(
                llm,
                user_question,
                results
            )


        # ----------------------------------
        # Display Answer
        # ----------------------------------

        with st.chat_message(
            "assistant"
        ):

            st.markdown(
                answer
            )


            # ----------------------------------
            # Show Retrieved Context
            # ----------------------------------

            with st.expander(
                "🔎 View Retrieved Context"
            ):

                for i, document in enumerate(
                    results
                ):

                    page_number = (
                        document.metadata.get(
                            "page",
                            "Unknown"
                        )
                    )

                    st.markdown(
                        f"**Result {i + 1} "
                        f"— Page {page_number}**"
                    )

                    st.write(
                        document.page_content
                    )

                    st.divider()


        # ----------------------------------
        # Save Assistant Response
        # ----------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "context": results
            }
        )


else:

    # ======================================
    # No PDF Uploaded
    # ======================================

    st.info(
        "👈 Please upload a PDF from the sidebar "
        "to start asking questions."
    )


    st.markdown(
        """
        ### 🚀 How it works

        1. 📄 Upload a Python PDF
        2. ✂️ Split the PDF into chunks
        3. 🧠 Generate Gemini embeddings
        4. 🗄️ Store vectors in ChromaDB
        5. 🔎 Retrieve relevant document chunks
        6. 🤖 Generate an answer using Gemini
        """
    )