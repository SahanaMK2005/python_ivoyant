import streamlit as st

from agent import agent


# ============================================================
# 1. Page Configuration
# ============================================================

st.set_page_config(
    page_title="AI Job Search Assistant",
    page_icon="💼",
    layout="centered"
)


# ============================================================
# 2. Application Title
# ============================================================

st.title("💼 AI Job Search Assistant")

st.write(
    "Find suitable jobs using an AI agent with "
    "job search and job suitability analysis tools."
)


# ============================================================
# 3. Example Query
# ============================================================

st.info(
    "Example: I am looking for a Python Backend Developer "
    "job in Bangalore. I have 2 years of experience and "
    "my skills are Python, FastAPI, SQL and Docker. "
    "I prefer remote jobs and my expected salary is 8 LPA."
)


# ============================================================
# 4. User Input
# ============================================================

user_query = st.text_area(
    "Describe the job you are looking for:",
    height=180,
    placeholder=(
        "Example:\n"
        "I am looking for a Python Backend Developer job "
        "in Bangalore..."
    )
)


# ============================================================
# 5. Search Button
# ============================================================

if st.button("🔍 Find Suitable Jobs", use_container_width=True):

    if not user_query.strip():

        st.warning("Please enter your job requirements.")

    else:

        # ====================================================
        # 6. Run AI Agent
        # ====================================================

        with st.spinner("🤖 AI Agent is searching for suitable jobs..."):

            try:

                result = agent.invoke(
                    {
                        "messages": [
                            {
                                "role": "user",
                                "content": user_query
                            }
                        ]
                    }
                )

                # ============================================
                # 7. Extract Final Agent Response
                # ============================================

                final_message = result["messages"][-1]

                content = final_message.content

                if isinstance(content, list):

                    text_parts = []

                    for item in content:

                        if (
                            isinstance(item, dict)
                            and item.get("type") == "text"
                        ):
                            text_parts.append(item["text"])

                    content = "\n".join(text_parts)

                # ============================================
                # 8. Display Result
                # ============================================

                st.success("Job analysis completed!")

                st.subheader("🤖 AI Recommendation")

                st.markdown(content)

            except Exception as e:

                st.error(
                    f"An error occurred while running the AI agent:\n\n{e}"
                )