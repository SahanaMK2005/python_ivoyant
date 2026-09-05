from google import genai

client = genai.Client()

text = "Smartphone with long-lasting battery and fast charging."

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=text
)

embedding = result.embeddings[0].values

print("Original text:")
print(text)

print("\nEmbedding generated successfully!")
print("Embedding dimensions:", len(embedding))
print("First 10 values:", embedding[:10])


