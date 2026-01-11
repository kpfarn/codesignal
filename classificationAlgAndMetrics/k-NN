import math
import matplotlib.pyplot as plt
import numpy as np

# k-Nearest Neighbors

def k_nearest_neighbors(data, query, k, distance_fn):
    neighbor_distances_and_indices = []
    for idx, label in enumerate(data):
        distance = distance_fn(label[0], query)
        neighbor_distances_and_indices.append((distance, idx))
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    k_nearest_labels = [data[i][1] for distance, i in k_nearest_distances_and_indices]
    return max(k_nearest_labels, key=k_nearest_labels.count)


def euclidean_distance(point1, point2):
    return math.sqrt(sum((p - q) ** 2 for p, q in zip(point1, point2)))

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
data = [
    ((2, 3), 'unripe'),
    ((5, 4), 'ripe'),
    ((9, 6), 'unripe'),
    ((4, 7), 'ripe'),
    ((8, 1), 'overripe'),
    ((7, 2), 'ripe'),
]

ripeness_label = k_nearest_neighbors(data, (7, 3), k=3, distance_fn=manhattan_distance)
print(ripeness_label)

features = np.array([item[0] for item in data])
labels = np.array([item[1] for item in data])

for ripeness in ['unripe', 'ripe', 'overripe']:
    plt.scatter(features[labels == ripeness, 0], features[labels == ripeness, 1], label=ripeness)

plt.scatter(7, 3, color='red', label='query', marker='x')
plt.legend()
plt.title('Fruits Classification with kNN')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
