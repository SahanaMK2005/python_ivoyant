import tiktoken

text = "what are you doing."

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode(text)

print("Original Text:")
print(text)

print("\nToken IDs:")
print(tokens)

print("\nTotal Number of Tokens Updated:")
print(len(tokens))

print("\nIndividual Tokens:")

for token in tokens:
    print(token, "->", repr(encoding.decode([token])))