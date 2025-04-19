def dfs_traverse(current, graph, visited, labels):
    """Recursive DFS traversal from the current node"""
    visited[current] = True
    print(labels[current], end=" ")

    for neighbor in range(len(graph)):
        if graph[current][neighbor] == 1 and not visited[neighbor]:
            dfs_traverse(neighbor, graph, visited, labels)

def run_dfs():
    nodes = 9
    graph = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    visited = [False] * nodes
    labels = ["watch", "shirt", "tie", "belt", "pants", "undershorts", "socks", "shoes", "jacket"]

    print("DFS Order:")
    for i in range(nodes):
        if not visited[i]:
            dfs_traverse(i, graph, visited, labels)

