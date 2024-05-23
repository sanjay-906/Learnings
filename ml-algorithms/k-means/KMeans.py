import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum(x1-x2)**2)

class KMeans:
    def __init__(self, k=5, max_iters= 100):
        self.k= k
        self.max_iters= max_iters
        self.clusters= [ [] for _ in range(self.k)]

        self.centroids= []

    def _closest_centroid(self, sample, centroids):
        distances= [euclidean_distance(sample, i) for i in centroids]
        return np.argmin(distances)

    def _create_clusters(self, centroids):
        clusters= [ [] for _ in range(self.k)]
        for i, sample in enumerate(self.X):
            centroid_index= self._closest_centroid(sample, centroids)
            clusters[centroid_index].append(i)
        return clusters

    def _get_centroids(self, clusters):
        centroids= np.zeros((self.k, self.n_features))
        for i, cluster in enumerate(clusters):
            cluster_mean= np.mean(self.X[cluster], axis= 0)
            centroids[i]= cluster_mean
        return centroids

    def _is_converged(self, old, new):
        distances= [euclidean_distance(new[i], old[i]) for i in range(self.k)]
        return sum(distances)==0

    def predict(self, X):
        self.X= X
        self.n, self.n_features= X.shape

        random_sample_idxs= np.random.choice(self.n, self.k, replace= False)

        self.centroids= [self.X[i] for i in random_sample_idxs]

        for _ in range(self.max_iters):
            self.clusters= self._create_clusters(self.centroids)
            centroids_old= self.centroids
            self.centroids= self._get_centroids(self.clusters)

            if self._is_converged(centroids_old, self.centroids):
                break


        return self._get_cluster_labels(self.clusters)

    def _get_cluster_labels(self, clusters):
        labels= np.empty(self.n)
        for i, cluster in enumerate(clusters):
            for j in cluster:
                labels[j]= i
        return labels

