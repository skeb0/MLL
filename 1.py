# Training data: (features, label)
training_data = [
    (['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes')
]

# Initialize hypothesis to the first positive example
hypothesis = training_data[0][0]

# Display the header
print(f"{'Example':<8} {'Training Example':<45} {'Hypothesis':<30}")

# Update hypothesis with each positive example and display
for i, (x, label) in enumerate(training_data, start=1):
    if label == 'Yes':
        hypothesis = ['?' if h != v else h for h, v in zip(hypothesis, x)]
    print(f"{i:<8} {str(x):<45} {str(hypothesis):<30}")

print("\nFinal Hypothesis:", hypothesis)
