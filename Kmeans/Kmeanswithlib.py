#kmeans with library
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
df=pd.read_csv('data.csv')
X = df.drop('Diabetes_binary',axis=1)
k = 2
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print("Centroids:")
print(centroids)
print("\nLabels:")
print(labels)
