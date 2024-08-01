from collections import Counter
import math

data = [
    ['Sunny', 'Hot', 'High', False, 'No'],
    ['Sunny', 'Hot', 'High', True, 'No'],
    ['Overcast', 'Hot', 'High', False, 'Yes'],
    ['Rain', 'Mild', 'High', False, 'Yes'],
    ['Rain', 'Cool', 'Normal', False, 'Yes'],
    ['Rain', 'Cool', 'Normal', True, 'No'],
    ['Overcast', 'Cool', 'Normal', True, 'Yes'],
    ['Sunny', 'Mild', 'High', False, 'No'],
    ['Sunny', 'Cool', 'Normal', False, 'Yes'],
    ['Rain', 'Mild', 'Normal', False, 'Yes'],
    ['Sunny', 'Mild', 'Normal', True, 'Yes'],
    ['Overcast', 'Mild', 'High', True, 'Yes'],
    ['Overcast', 'Hot', 'Normal', False, 'Yes'],
    ['Rain', 'Mild', 'High', True, 'No']
]
attributes = ['Outlook', 'Temperature', 'Humidity', 'Windy']

def entropy(examples):
    labels = [row[-1] for row in examples]
    counts = Counter(labels)
    return -sum((count / len(labels)) * math.log2(count / len(labels)) for count in counts.values())

def info_gain(examples, index):
    total_entropy = entropy(examples)
    values = set(row[index] for row in examples)
    subset_entropy = sum((sum(1 for row in examples if row[index] == v) / len(examples)) *
                         entropy([row for row in examples if row[index] == v]) for v in values)
    return total_entropy - subset_entropy

def id3(examples, attrs):
    if len(set(row[-1] for row in examples)) == 1:
        return examples[0][-1]
    if not attrs:
        return Counter(row[-1] for row in examples).most_common(1)[0][0]

    best_attr = max(attrs, key=lambda a: info_gain(examples, attributes.index(a)))
    tree = {best_attr: {}}
    for val in set(row[attributes.index(best_attr)] for row in examples):
        subtree = id3([row for row in examples if row[attributes.index(best_attr)] == val],
                      [a for a in attrs if a != best_attr])
        tree[best_attr][val] = subtree
    return tree

decision_tree = id3(data, attributes)
print(decision_tree)

sample = ['Sunny', 'Cool', 'High', True]  
def classify(tree, sample):
    if not isinstance(tree, dict):
        return tree
    attr = next(iter(tree))
    value = sample[attributes.index(attr)]
    return classify(tree[attr][value], sample)

print("Classified as:", classify(decision_tree, sample))
