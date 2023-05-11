import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


class PAM:

    def __init__(self, n_clusters=3, max_iter=300, distance_metric="euclidean"):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.distance_metric = distance_metric

    def _euclidean_distance(self, a, b):
        return np.sqrt(np.sum((a - b) ** 2, axis=1))

    def _squared_euclidean_distance(self, a, b):
        return np.sum((a - b) ** 2, axis=1)

    def _chebyshev_distance(self, a, b):
        return np.max(np.abs(a - b), axis=1)

    def _power_distance(self, a, b, p=3):
        return np.sum(np.abs(a - b) ** p, axis=1) ** (1 / p)

    def _compute_distances(self, X, medoids):
        distances = []
        for medoid in medoids:
            if self.distance_metric == "euclidean":
                distance = self._euclidean_distance(X, medoid)
            elif self.distance_metric == "squared_euclidean":
                distance = self._squared_euclidean_distance(X, medoid)
            elif self.distance_metric == "chebyshev":
                distance = self._chebyshev_distance(X, medoid)
            elif self.distance_metric == "power":
                distance = self._power_distance(X, medoid)
            else:
                raise ValueError("Invalid distance metric")
            distances.append(distance)
        return np.array(distances).T

    def fit(self, X):
        self.medoids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iter):
            distances = self._compute_distances(X, self.medoids)
            self.labels = np.argmin(distances, axis=1)
            new_medoids = np.array(
                [X[self.labels == i][np.argmin(self._compute_distances(X[self.labels == i], X[self.labels == i]))] for i
                 in range(self.n_clusters)])
            if np.allclose(self.medoids, new_medoids, atol=1e-4):
                break
            self.medoids = new_medoids

        self.inertia_ = np.sum([np.sum(distances[self.labels == i, i]) for i in range(self.n_clusters)])

    def predict(self, X):
        distances = self._compute_distances(X, self.medoids)
        return np.argmin(distances, axis=1)

    def fit_predict(self, X):
        self.fit(X)
        return self.labels


# Создание случайных точек на плоскости
X, y = make_blobs(n_samples=300, centers=4, random_state=1)


def plot_elbow(X, max_clusters=10):
    distortions = []
    for i in range(1, max_clusters + 1):
        km = PAM(n_clusters=i)
        km.fit(X)
        distortions.append(km.inertia_)
    plt.plot(range(1, max_clusters + 1), distortions, marker='o')
    plt.xlabel("Количество кластеров")
    plt.ylabel("Сумма квадратов ошибок (SSE)")
    plt.show()


# Определение оптимального количества кластеров с помощью метода локтя
plot_elbow(X)


# Применение алгоритма кластеризации с разными начальными значениями центров и количеством кластеров,
# а также с разными мерами расстояния:
def plot_clusters(X, y_pred, centroids):
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap="viridis")
    plt.scatter(centroids[:, 0], centroids[:, 1], c="red", marker="x", s=200)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Результат кластеризации")
    plt.show()


# Пример использования класса KMeans с разными начальными значениями центров и количеством кластеров
km = PAM(n_clusters=4, distance_metric="euclidean")
y_pred = km.fit_predict(X)
plot_clusters(X, y_pred, km.medoids)

# Пример использования класса KMeans с разными мерами расстояния
distance_metrics = ["euclidean", "squared_euclidean", "chebyshev", "power"]
for metric in distance_metrics:
    km = PAM(n_clusters=4, distance_metric=metric)
    y_pred = km.fit_predict(X)
    print(f"Результат кластеризации с мерой расстояния {metric}:")
    plot_clusters(X, y_pred, km.medoids)
