def topological_sort_util(v, visited, stack, graph):
    visited[v] = True
    for i in range(len(graph)):
        if graph[v][i] and not visited[i]:
            topological_sort_util(i, visited, stack, graph)
    stack.append(v)

def run_topological_sort():
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
    labels = ["watch", "shirt", "tie", "belt", "pants", "undershorts", "socks", "shoes", "jacket"]
    visited = [False] * len(graph)
    stack = []

    for i in range(len(graph)):
        if not visited[i]:
            topological_sort_util(i, visited, stack, graph)

    print("\nTopological Sort Order:")
    while stack:
        print(labels[stack.pop()], end=" ")
