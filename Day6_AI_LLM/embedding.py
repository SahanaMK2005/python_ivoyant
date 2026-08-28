from google import genai
import math

client = genai.Client()


def get_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


def cosine_similarity(vector_a, vector_b):
    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    return dot_product / (magnitude_a * magnitude_b)


# Example sentences
sentences = [
    "I love programming in Python.",
    "Python programming is something I enjoy.",
    "I like eating pizza."
]


# Generate embeddings
embeddings = []

print("=" * 60)
print("EMBEDDING GENERATION")
print("=" * 60)

for sentence in sentences:

    embedding = get_embedding(sentence)

    embeddings.append(embedding)

    print("\nSentence:")
    print(sentence)

    print("Embedding dimensions:", len(embedding))

    print("First 10 values:")
    print(embedding[:10])


# Compare sentences
print("\n" + "=" * 60)
print("SEMANTIC SIMILARITY")
print("=" * 60)

similarity_1_2 = cosine_similarity(
    embeddings[0],
    embeddings[1]
)

similarity_1_3 = cosine_similarity(
    embeddings[0],
    embeddings[2]
)

print("\nSentence 1:")
print(sentences[0])

print("\nSentence 2:")
print(sentences[1])

print("\nSimilarity:")
print(similarity_1_2)


print("\n" + "-" * 60)

print("\nSentence 1:")
print(sentences[0])

print("\nSentence 3:")
print(sentences[2])

print("\nSimilarity:")
print(similarity_1_3)


# Identify the more similar sentence
print("\n" + "=" * 60)
print("RESULT")
print("=" * 60)

if similarity_1_2 > similarity_1_3:
    print(
        "Sentence 1 and Sentence 2 are more "
        "semantically similar."
    )
else:
    print(
        "Sentence 1 and Sentence 3 are more "
        "semantically similar."
    )