import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets
from sklearn.cluster import KMeans 
from sklearn.mixture import GaussianMixture 
from sklearn import metrics 
import pandas as pd

iris = datasets.load_iris() 
X = pd.DataFrame(iris.data) 
X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'] 
y = pd.DataFrame(iris.target) 
y.columns = ['Targets'] 

kmeans_model = KMeans(n_clusters=3, random_state=0) 
kmeans_model.fit(X) 
kmeans_labels = kmeans_model.labels_

plt.figure(figsize=(14, 7)) 
colormap = np.array(['red', 'lime', 'black']) 
plt.subplot(1, 2, 1) 
plt.scatter(X['Petal_Length'], X['Petal_Width'], c=colormap[kmeans_labels], s=40) 
plt.title('K-Means Clustering') 
plt.xlabel('Petal Length') 
plt.ylabel('Petal Width') 

gmm = GaussianMixture(n_components=3, random_state=0).fit(X) 
gmm_labels = gmm.predict(X)

plt.subplot(1, 2, 2) 
plt.scatter(X['Petal_Length'], X['Petal_Width'], c=colormap[gmm_labels], s=40) 
plt.title('GMM Clustering') 
plt.xlabel('Petal Length') 
plt.ylabel('Petal Width') 

silhouette_kmeans = metrics.silhouette_score(X, kmeans_labels) 
silhouette_gmm = metrics.silhouette_score(X, gmm_labels) 
print("Silhouette Score (K-Means):", silhouette_kmeans) 
print("Silhouette Score (GMM):", silhouette_gmm) 

plt.show()
