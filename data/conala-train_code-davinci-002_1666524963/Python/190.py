from sklearn.cluster import KMeans
import numpy as np

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
kmeans = KMeans(n_clusters=3, random_state=0).fit(X.reshape(-1, 1))
print(kmeans.labels_)