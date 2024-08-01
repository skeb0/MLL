from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
import matplotlib.pyplot as plt

cancer = load_breast_cancer()
X, y = cancer.data[:, :2], cancer.target

svm = SVC(kernel='rbf', gamma=0.5, C=1.0).fit(X, y)

DecisionBoundaryDisplay.from_estimator(svm, X, response_method='predict', cmap=plt.cm.Spectral, alpha=0.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolors='k')
plt.xlabel(cancer.feature_names[0])
plt.ylabel(cancer.feature_names[1])
plt.show()
