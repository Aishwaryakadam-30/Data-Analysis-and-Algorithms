from typing import List
import numpy as np

def floyd_warshall(weight_matrix: List[List[int]]):
    W = np.array(weight_matrix)
    V = len(W)
    D = np.zeros((V, V, V))
    D[0] = W

    for k in range(V - 1):
        next_k = k + 1
        for i in range(V):
            for j in range(V):
                D[next_k][i][j] = min(D[k][i][j], D[k][i][k] + D[k][k][j])
        print(f"\nDistance Matrix D{next_k}")
        print(D[next_k])
    return D[V - 1]

def floyd_warshall_recursive(matrix: List[List[int]], k: int):
    V = len(matrix)
    updated = np.zeros((V, V))
    for i in range(V):
        for j in range(V):
            updated[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    print(f"\nDistance Matrix D{k + 1}")
    print(updated)
    if k == V - 1:
        return updated
    return floyd_warshall_recursive(updated, k + 1)

def generate_parents(weights: List[List[int]]):
    V = len(weights)
    parent = [[None for _ in range(V)] for _ in range(V)]
    for i in range(V):
        for j in range(V):
            if i != j and weights[i][j] != float('inf'):
                parent[i][j] = i
    return np.array(parent)

if __name__ == "__main__":
    W = [
        [0, 3, 8, float('inf'), -4],
        [float('inf'), 0, float('inf'), 1, 7],
        [float('inf'), 4, 0, float('inf'), float('inf')],
        [2, float('inf'), -5, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0]
    ]

    print("\n--- Floyd-Warshall Iterative ---")
    print("Final Distance Matrix:\n", floyd_warshall(W))

    print("\n--- Floyd-Warshall Recursive ---")
    print("Final Distance Matrix:\n", floyd_warshall_recursive(W, 0))

    print("\n--- Parent Matrix ---")
    print(generate_parents(W))
