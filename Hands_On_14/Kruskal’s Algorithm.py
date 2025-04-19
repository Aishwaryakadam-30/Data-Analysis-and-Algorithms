class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            return True
        return False

def run_kruskal():
    matrix = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 0, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    size = len(matrix)
    edges = []

    for i in range(size):
        for j in range(i+1, size):
            if matrix[i][j]:
                edges.append(Edge(i, j, matrix[i][j]))

    edges.sort(key=lambda e: e.weight)
    uf = UnionFind(size)
    print("\nMinimum Spanning Tree (Kruskal):")
    for edge in edges:
        if uf.union(edge.src, edge.dest):
            print(f"{vertices[edge.src]} -- {vertices[edge.dest]} : {edge.weight}")
