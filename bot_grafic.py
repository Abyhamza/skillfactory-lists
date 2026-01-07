import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import Birch

# Генерация случайных данных
X, y = make_blobs(n_samples=1000, centers=4, cluster_std=0.60, random_state=0)

# Создание модели BIRCH
birch_model = Birch(n_clusters=4)  # n_clusters - предполагаемое количество кластеров
birch_model.fit(X)

# Предсказание кластеров для данных
y_birch = birch_model.predict(X)

# Визуализация кластеров
plt.scatter(X[:, 0], X[:, 1], c=y_birch, cmap='viridis', marker='o', edgecolor='k', s=30)
plt.title('Результаты кластеризации с использованием алгоритма BIRCH')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.show()
