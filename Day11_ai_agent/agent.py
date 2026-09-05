import os

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

from tools import search_jobs, analyze_job_suitability


# ============================================================
# 1. Check Gemini API key
# ============================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set."
    )


# ============================================================
# 2. Initialize Gemini LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


# ============================================================
# 3. Define Tool 1 - Job Search
# ============================================================

@tool
def job_search_tool(
    title: str = "",
    location: str = "",
    skills: list[str] | None = None,
    remote: bool = False
):
    """
    Search the local job database for jobs matching
    title, location, skills, and remote preference.
    """

    return search_jobs(
        title=title,
        location=location,
        skills=skills,
        remote=remote
    )


# ============================================================
# 4. Define Tool 2 - Job Suitability Analysis
# ============================================================

@tool
def job_suitability_tool(
    job: dict,
    experience: int,
    skills: list[str],
    expected_salary: int,
    remote_preference: bool = False
):
    """
    Analyze how suitable a job is for a candidate based
    on experience, skills, salary, and remote preference.
    """

    return analyze_job_suitability(
        job=job,
        experience=experience,
        skills=skills,
        expected_salary=expected_salary,
        remote_preference=remote_preference
    )


# ============================================================
# 5. Register Both Tools
# ============================================================

tools = [
    job_search_tool,
    job_suitability_tool
]


# ============================================================
# 6. Create the AI Agent
# ============================================================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
You are a Job Search Assistant.

Your job is to help users find suitable jobs from the
available job database.

You have two tools:

1. job_search_tool
   - Searches the job database.
   - Use this when the user wants to find jobs.

2. job_suitability_tool
   - Analyzes how suitable a job is for a candidate.
   - Use this when candidate information such as experience,
     skills, salary expectation, or remote preference is available.

When the user provides detailed job requirements:

1. Understand the user's requirements.
2. Use job_search_tool to find relevant jobs.
3. Analyze suitable jobs using job_suitability_tool.
4. Compare the results.
5. Recommend the best matching jobs.
6. Explain the recommendation clearly.

Do not invent jobs or job information.
Use information returned by the tools.

If no jobs are found, clearly tell the user that no matching
jobs were found.
"""
)


# ============================================================
# 7. Run the Agent
# ============================================================

if __name__ == "__main__":

    user_query = """
    I am looking for a Python Backend Developer job in Bangalore.
    I have 2 years of experience and my skills are Python, FastAPI,
    SQL and Docker.

    I prefer remote jobs and my expected salary is 8 LPA.
    Find suitable jobs and tell me which one is the best match.
    """

    print("\nUser:")
    print(user_query)

    print("\nAgent is working...\n")

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


    # ========================================================
    # 8. Display Agent Trace
    # ========================================================

    print("\n========== AGENT TRACE ==========\n")

    for message in result["messages"]:

        print("MESSAGE TYPE:", type(message).__name__)

        if hasattr(message, "tool_calls") and message.tool_calls:
            print("TOOL CALLS:")
            print(message.tool_calls)

        if hasattr(message, "content") and message.content:
            print("CONTENT:")
            print(message.content)

        print("\n-----------------------------\n")


    # ========================================================
    # 9. Extract and Display Final Answer
    # ========================================================

    print("\n========== FINAL ANSWER ==========\n")

    final_message = result["messages"][-1]

    content = final_message.content

    # Gemini may return the content as a list of content blocks.
    if isinstance(content, list):

        for item in content:

            if isinstance(item, dict) and item.get("type") == "text":

                print(item["text"])

    else:

        print(content)