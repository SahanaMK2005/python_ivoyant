import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-5-mini",
    input="Explain Machine Learning in simple words."
)

print("Response:")
print(response.output_text)

print("\nToken Usage:")
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)