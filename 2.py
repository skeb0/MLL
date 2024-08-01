training_data = [
    (['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes')
]

S = ['0'] * len(training_data[0][0])  
G = [['?'] * len(S)] 

print("The initial value of hypothesis:")
print(f"The most specific hypothesis S0: {S}")
print(f"The most general hypothesis G0: {G}\n")

print("Candidate Elimination algorithm")

for i, (x, label) in enumerate(training_data, start=1):
    if label == 'Yes':
        S = ['?' if s != v and s != '0' else v for s, v in zip(S, x)]
        G = [g for g in G if all(g[i] == '?' or g[i] == x[i] for i in range(len(S)))]
    else:
        G = [g for g in G for j in range(len(g)) if g[j] == '?' and g[:j] + [x[j]] + g[j+1:] not in G]

    print(f"For Training Example No :{i} the hypothesis is S{i} {S}")
    print(f"For Training Example No :{i} the hypothesis is G{i} {G}\n")

print("Final Hypothesis:")
print(f"S: {S}")
print(f"G: {G}")
