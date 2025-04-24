import numpy as np

def floyd_warshall(weight_matrix):
    n = len(weight_matrix)
    dist = np.array(weight_matrix, dtype=float)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
        print(f"\nD{k + 1} Matrix:")
        print(dist)
    return dist

def create_parent_matrix(weights):
    n = len(weights)
    parent = [[None if i == j or weights[i][j] == float('inf') else i for j in range(n)] for i in range(n)]
    return parent

if __name__ == '__main__':
    W = [
        [0, 3, 8, float('inf'), -4],
        [float('inf'), 0, float('inf'), 1, 7],
        [float('inf'), 4, 0, float('inf'), float('inf')],
        [2, float('inf'), -5, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0]
    ]
    print("Final Distance Matrix:\n", floyd_warshall(W))
    print("\nParent Matrix:")
    print(np.array(create_parent_matrix(W)))
