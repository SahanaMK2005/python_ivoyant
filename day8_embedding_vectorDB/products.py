products = [
    "Smartphone with long-lasting battery and fast charging.",
    "Wireless headphones with advanced noise cancellation.",
    "Lightweight laptop designed for programming and software development.",
    "Running shoes with comfortable cushioning for long-distance running.",
    "Smartwatch with accurate fitness and heart-rate tracking.",
    "Gaming laptop with a powerful processor and dedicated graphics.",
    "Bluetooth speaker with powerful bass and clear sound.",
    "Smartphone with an advanced camera and high-resolution display.",
    "Laptop with long battery life for students and professionals.",
    "Fitness band for monitoring daily steps and sleep patterns.",
    "Wireless earbuds with clear audio and a comfortable fit.",
    "Tablet with a large display for reading and entertainment.",
    "Office chair with ergonomic lumbar support.",
    "Mechanical keyboard designed for gaming and fast typing.",
    "4K television with vivid colors and smart streaming features.",
    "Digital camera with high-quality images for travel photography.",
    "Running watch with GPS and workout tracking.",
    "Portable power bank with fast charging support.",
    "Noise-cancelling headphones designed for comfortable travel.",
    "Smartphone with a powerful processor for mobile gaming."
]

if __name__ == "__main__":
    print("Number of products:", len(products))

    for i, product in enumerate(products, start=1):
        print(f"{i}. {product}")