import os
from google import genai


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set."
    )


client = genai.Client(
    api_key=api_key
)


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what RAG is in one sentence."
)


print("=" * 60)
print("GEMINI TEST")
print("=" * 60)

print(response.text)