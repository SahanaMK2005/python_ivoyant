from google import genai

client = genai.Client()


response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain Machine Learning in simple words."
)

print("Response:")
print(response.text)

print("\nToken Usage:")

if response.usage_metadata:
    print("Input tokens:", response.usage_metadata.prompt_token_count)
    print("Output tokens:", response.usage_metadata.candidates_token_count)
    print("Total tokens:", response.usage_metadata.total_token_count)