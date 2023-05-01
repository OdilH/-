import numpy as np
import matplotlib.pyplot as plt


class Hamelion:
    def __init__(self, epsilon, min_samples):
        self.epsilon = epsilon
        self.min_samples = min_samples
        self.labels_ = None
        self.core_samples_indices_ = None
        self.components_ = None
        self.core_samples_mask_ = None
        self.n_clusters_ = None

    def fit(self, X):
        n_samples, n_features = X.shape
        distances = np.zeros((n_samples, n_samples))
        for i in range(n_samples):
            for j in range(i + 1, n_samples):
                distances[i, j] = np.linalg.norm(X[i] - X[j])
                distances[j, i] = distances[i, j]

        seeds = []
        visited = np.zeros(n_samples)
        for sample_index in range(n_samples):
            if visited[sample_index]:
                continue
            neighbor_indices = np.where(distances[sample_index] < self.epsilon)[0]
            if len(neighbor_indices) >= self.min_samples:
                seeds.append(sample_index)
                visited[sample_index] = 1
                for neighbor_index in neighbor_indices:
                    visited[neighbor_index] = 1

        seed_indices_mask = np.zeros(n_samples, dtype=bool)
        seed_indices_mask[seeds] = True
        self.core_samples_mask_ = seed_indices_mask
        self.labels_ = np.zeros(n_samples)
        self.n_clusters_ = 0
        for seed_index in seeds:
            if self.labels_[seed_index] == 0:
                self.n_clusters_ += 1
                self._expand_cluster(X, seed_index, distances, self.labels_, self.n_clusters_)

        self.core_samples_indices_ = np.arange(n_samples)[self.core_samples_mask_]
        self.components_ = [X[self.labels_ == i] for i in range(1, self.n_clusters_ + 1)]


    def _expand_cluster(self, X, seed_index, distances, labels, cluster_label):
        labels[seed_index] = cluster_label
        indices = np.where(distances[seed_index] < self.epsilon)[0]
        for index in indices:
            if labels[index] == 0:
                labels[index] = cluster_label
                if self.core_samples_mask_[index]:
                    self._expand_cluster(X, index, distances, labels, cluster_label)

    