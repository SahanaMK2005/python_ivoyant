import tiktoken

text = "What are you doing? I am learning Python and Large Language Models."

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("Original Text:")
print(text)

print("\nToken IDs:")
print(tokens)

print("\nTotal Number of Tokens:")
print(len(tokens))

print("\nIndividual Tokens:")

for token in tokens:
    decoded_token = encoding.decode([token])
    print(token, "->", repr(decoded_token))