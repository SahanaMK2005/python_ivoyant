import streamlit as st
import requests


# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Customer Support Assistant",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------------
# API URL
# -----------------------------------

API_URL = "http://127.0.0.1:8000"


# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "🤖 Customer Support",
        "🧑‍💼 Knowledge Management"
    ]
)


# ===================================
# CUSTOMER SUPPORT MODULE
# ===================================

if page == "🤖 Customer Support":

    st.title("🤖 AI Customer Support Assistant")

    st.write(
        "Ask any question related to company policies, refunds, "
        "returns, shipping, and other services."
    )

    st.divider()


    # -----------------------------------
    # QUESTION INPUT
    # -----------------------------------

    question = st.text_input(
        "Ask your question",
        placeholder="Example: What is the return policy?"
    )


    # -----------------------------------
    # SEND QUESTION
    # -----------------------------------

    if st.button("Send"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            try:

                with st.spinner(
                    "Searching knowledge base and generating AI response..."
                ):

                    response = requests.get(

                        f"{API_URL}/ask",

                        params={
                            "question": question
                        },

                        timeout=60
                    )


                # -----------------------------------
                # SUCCESS RESPONSE
                # -----------------------------------

                if response.status_code == 200:

                    data = response.json()


                    # ---------------------------
                    # AI RESPONSE
                    # ---------------------------

                    st.subheader("🤖 AI Response")

                    st.success(
                        data["answer"]
                    )


                    # ---------------------------
                    # RETRIEVED KNOWLEDGE
                    # ---------------------------

                    st.subheader("📚 Retrieved Knowledge")

                    for knowledge in data["retrieved_knowledge"]:

                        st.write(
                            f"• {knowledge}"
                        )


                else:

                    st.error(
                        f"API Error: {response.status_code}"
                    )


            except requests.exceptions.Timeout:

                st.error(
                    "The AI response is taking too long. "
                    "Please try again."
                )


            except requests.exceptions.ConnectionError:

                st.error(
                    "Unable to connect to FastAPI. "
                    "Please make sure the FastAPI server is running."
                )


            except Exception as e:

                st.error(
                    f"An error occurred: {str(e)}"
                )


# ===================================
# KNOWLEDGE MANAGEMENT MODULE
# ===================================

elif page == "🧑‍💼 Knowledge Management":

    st.title("🧑‍💼 Knowledge Management")

    st.write(
        "Manage company policies and knowledge used by "
        "the AI Customer Support Assistant."
    )

    st.divider()


    # -----------------------------------
    # GET ALL KNOWLEDGE
    # -----------------------------------

    try:

        response = requests.get(

            f"{API_URL}/knowledge",

            timeout=20
        )


        # -----------------------------------
        # SUCCESS RESPONSE
        # -----------------------------------

        if response.status_code == 200:

            data = response.json()


            st.subheader("📚 Available Knowledge")


            # -----------------------------------
            # DISPLAY KNOWLEDGE
            # -----------------------------------

            for item in data["data"]:


                # Each knowledge item
                with st.expander(

                    f"{item['id']}. {item['category']}"

                ):


                    # ---------------------------
                    # EDIT CATEGORY
                    # ---------------------------

                    category = st.text_input(

                        "Category",

                        value=item["category"],

                        key=f"category_{item['id']}"

                    )


                    # ---------------------------
                    # EDIT CONTENT
                    # ---------------------------

                    content = st.text_area(

                        "Content",

                        value=item["content"],

                        height=150,

                        key=f"content_{item['id']}"

                    )


                    # ---------------------------
                    # UPDATE BUTTON
                    # ---------------------------

                    if st.button(

                        "💾 Update Knowledge",

                        key=f"update_{item['id']}"

                    ):


                        # ---------------------------
                        # VALIDATION
                        # ---------------------------

                        if (

                            category.strip() == ""

                            or

                            content.strip() == ""

                        ):

                            st.warning(

                                "Category and content cannot be empty."

                            )


                        else:

                            try:


                                # ---------------------------
                                # CALL FASTAPI PUT API
                                # ---------------------------

                                update_response = requests.put(

                                    f"{API_URL}/knowledge/{item['id']}",

                                    json={

                                        "category": category,

                                        "content": content

                                    },

                                    timeout=20

                                )


                                # ---------------------------
                                # SUCCESS
                                # ---------------------------

                                if (

                                    update_response.status_code

                                    == 200

                                ):

                                    st.success(

                                        "Knowledge updated successfully!"

                                    )

                                    st.info(

                                        "The updated knowledge has been "
                                        "saved to knowledge.json. "
                                        "APScheduler will synchronize it "
                                        "with ChromaDB automatically."

                                    )


                                    # Refresh Streamlit page

                                    st.rerun()


                                # ---------------------------
                                # ERROR
                                # ---------------------------

                                else:

                                    st.error(

                                        f"Update failed: "
                                        f"{update_response.status_code}"

                                    )


                            except Exception as e:

                                st.error(

                                    f"Unable to update knowledge: "
                                    f"{str(e)}"

                                )


        else:

            st.error(

                "Unable to retrieve knowledge."

            )


    except requests.exceptions.ConnectionError:

        st.error(

            "Unable to connect to FastAPI. "
            "Please make sure the FastAPI server is running."

        )


    except Exception as e:

        st.error(

            f"An error occurred: {str(e)}"

        )