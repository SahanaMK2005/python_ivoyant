from google import genai
import tiktoken

client = genai.Client()

context = """
Python is a high-level programming language.
Python is widely used for web development.
Python is used for automation.
Python is used for data analysis.
Python is used for machine learning.
Python is used for artificial intelligence.

Python has a simple and readable syntax.
Python supports object-oriented programming.
Python supports functional programming.
Python has a large standard library.

Python is commonly used with libraries and frameworks.
NumPy is used for numerical computing.
Pandas is used for data analysis.
Scikit-learn is used for machine learning.
PyTorch is used for deep learning.
FastAPI is used for building APIs.

Python is widely used by developers and data scientists.
It can be used to create web applications.
It can be used to build automation scripts.
It can be used to process and analyze data.
It can be used to build machine learning applications.
It can also be used to build artificial intelligence applications.
"""

question = "What is Python used for?"

prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

encoding = tiktoken.get_encoding("cl100k_base")

estimated_tokens = len(encoding.encode(prompt))

print("Estimated prompt tokens:", estimated_tokens)
print("Prompt characters:", len(prompt))

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print("Response:")
print(response.text)

print("\nToken Usage:")

if response.usage_metadata:
    print("Input tokens:",
          response.usage_metadata.prompt_token_count)

    print("Output tokens:",
          response.usage_metadata.candidates_token_count)

    print("Total tokens:",
          response.usage_metadata.total_token_count)