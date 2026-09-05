from google import genai

client = genai.Client()

EMBEDDING_MODEL = "gemini-embedding-001"


def generate_embedding(text):
    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return result.embeddings[0].values


if __name__ == "__main__":
    text = "Smartphone with long-lasting battery and fast charging."

    vector = generate_embedding(text)

    print("Text:")
    print(text)

    print("\nEmbedding generated successfully!")
    print("Dimensions:", len(vector))
    print("First 5 values:", vector[:5])