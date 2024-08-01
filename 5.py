from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X, y = data.data, data.target

train_size = 514
test_size = 254
if len(X) < (train_size + test_size):
    train_size = int(len(X) * 0.67)
    test_size = len(X) - train_size

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, test_size=test_size, random_state=42)

model = GaussianNB().fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

print(f'Accuracy: {accuracy * 100:.8f}%')
