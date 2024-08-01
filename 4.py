import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

inputs = np.array([[0.66666667, 1.0],
                   [0.33333333, 0.55555556],
                   [1.0, 0.66666667]])

actual_output = np.array([[0.92], [0.86], [0.89]])

weights = np.random.rand(2, 1)

for _ in range(10000):
    input_layer = inputs
    predictions = sigmoid(np.dot(input_layer, weights))
    error = actual_output - predictions
    adjustments = error * sigmoid_derivative(predictions)
    weights += np.dot(input_layer.T, adjustments)

print("Input:\n", inputs)
print("\nActual Output:\n", actual_output)
print("\nPredicted Output:\n", predictions)
