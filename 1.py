training_data = [
    (['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes')
]

hypothesis = training_data[0][0]

print(f"{'Example':<8} {'Training Example':<45} {'Hypothesis':<30}")

for i, (x, label) in enumerate(training_data, start=1):
    if label == 'Yes':
        hypothesis = ['?' if h != v else h for h, v in zip(hypothesis, x)]
    print(f"{i:<8} {str(x):<45} {str(hypothesis):<30}")

print("\nFinal Hypothesis:", hypothesis)
