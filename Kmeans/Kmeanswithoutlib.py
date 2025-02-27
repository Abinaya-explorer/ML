#kmeans without library:
import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
df = pd.read_csv('data.csv')

X = df.drop('Diabetes_binary', axis=1).values
def kmeans(X, k, max_iters=100):
    centroids = X[np.random.choice(range(len(X)), k, replace=False)]
    for _ in range(max_iters):
        labels = np.argmin(np.linalg.norm(X[:, np.newaxis] - centroids, axis=2), axis=1)
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    silhouette_avg = silhouette_score(X, labels)
    return centroids, labels, silhouette_avg
k = 2
centroids, labels, silhouette_avg = kmeans(X, k)

print("Centroids:")
print(centroids)
print("\nLabels:")
print(labels)
print("\nSilhouette Score:", silhouette_avg)
