import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.manifold import MDS
from sklearn.cluster import AgglomerativeClustering


class Chameleon:
    def __init__(self, k=5, m=10, p=0.5):
        self.k = k  # число ближайших соседей для рассмотрения
        self.m = m  # число ближайших соседей для построения графа
        self.p = p  # пороговое значение для определения сильной связи
        self.labels_ = None  # метки кластеров после кластеризации

    def fit_predict(self, X):
        # вычисляем матрицу расстояний между объектами
        dists = pairwise_distances(X)

        # строим граф на основе m ближайших соседей
        graph = np.zeros_like(dists)
        for i in range(X.shape[0]):
            idx = np.argsort(dists[i])[1:self.m + 1]
            graph[i, idx] = 1
            graph[idx, i] = 1

        # находим сильные связи в графе
        strong_links = np.zeros_like(graph)
        for i in range(X.shape[0]):
            for j in range(i + 1, X.shape[0]):
                if graph[i, j] == 1 and self._is_strong_link(i, j, graph, dists):
                    strong_links[i, j] = 1
                    strong_links[j, i] = 1

        # вычисляем матрицу сходства между объектами
        sim = np.zeros_like(dists)
        for i in range(X.shape[0]):
            for j in range(i + 1, X.shape[0]):
                sim[i, j] = self._similarity(i, j, strong_links, dists)
                sim[j, i] = sim[i, j]

        # применяем MDS для снижения размерности
        embedding = MDS(n_components=2, dissimilarity='precomputed').fit_transform(sim)

        # применяем Agglomerative Clustering для кластеризации
        agg = AgglomerativeClustering(n_clusters=self.k, linkage='ward')
        self.labels_ = agg.fit_predict(embedding)

        return self.labels_

    def _is_strong_link(self, i, j, graph, dists):
        # проверяем, является ли связь между i и j сильной
        nn_i = np.argsort(dists[i])[1:self.k + 1]
        nn_j = np.argsort(dists[j])[1:self.k + 1]
        num_shared = len(set(nn_i) & set(nn_j))
        num_total = len(set(nn_i) | set(nn_j))
        if num_shared / num_total >= self.p:
            return True
        else:
            return False

    def _similarity(self, i, j, strong_links, dists):
        # находим ближайших соседей для i и j
        nn_i = np.argsort(dists[i])[1:self.k + 1]
        nn_j = np.argsort(dists[j])[1:self.k + 1]

        # вычисляем сходство по формуле из статьи
        num_common_links = np.sum(strong_links[i, nn_i] * strong_links[j, nn_j])
        num_total_links = np.sum(strong_links[i, nn_i]) + np.sum(strong_links[j, nn_j])
        if num_total_links > 0:
            sim = num_common_links / num_total_links
        else:
            sim = 0

        return sim


import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# генерируем искусственные данные
X, _ = make_blobs(n_samples=100, centers=3, random_state=42)

# создаем объект Chameleon и кластеризуем данные
chameleon = Chameleon(k=3, m=10, p=0.5)
labels = chameleon.fit_predict(X)

# отображаем результаты на графике
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.show()
