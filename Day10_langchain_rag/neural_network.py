import numpy as np


# ==========================================
# Activation Function
# ==========================================

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))


# ==========================================
# Neural Network Parameters
# ==========================================

# Input layer
X = np.array([
    [0.5],
    [0.8]
])


# Weights from input layer → hidden layer
W1 = np.array([
    [0.4, 0.3],
    [0.6, 0.7]
])


# Bias for hidden layer
b1 = np.array([
    [0.1],
    [0.2]
])


# Weights from hidden layer → output layer
W2 = np.array([
    [0.5, 0.8]
])


# Bias for output layer
b2 = np.array([
    [0.1]
])


# ==========================================
# Forward Pass
# ==========================================

print("=" * 60)
print("NEURAL NETWORK FORWARD PASS")
print("=" * 60)


# ------------------------------------------
# Step 1: Input
# ------------------------------------------

print("\nInput:")
print(X)


# ------------------------------------------
# Step 2: Input → Hidden Layer
# ------------------------------------------

z1 = np.dot(W1.T, X) + b1

print("\nHidden Layer Weighted Sum (z1):")
print(z1)


# ------------------------------------------
# Step 3: Hidden Layer Activation
# ------------------------------------------

a1 = sigmoid(z1)

print("\nHidden Layer Activation (a1):")
print(a1)


# ------------------------------------------
# Step 4: Hidden → Output Layer
# ------------------------------------------

z2 = np.dot(W2, a1) + b2

print("\nOutput Layer Weighted Sum (z2):")
print(z2)


# ------------------------------------------
# Step 5: Output Activation
# ------------------------------------------

output = sigmoid(z2)

print("\nFinal Output:")
print(output)


# ==========================================
# Prediction
# ==========================================

if output[0][0] >= 0.5:
    prediction = 1
else:
    prediction = 0


print("\nPrediction:", prediction)

print("\n" + "=" * 60)
print("FORWARD PASS COMPLETED")
print("=" * 60)