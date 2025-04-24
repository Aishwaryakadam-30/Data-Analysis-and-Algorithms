class Edge:
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost

class Vertex:
    def __init__(self, id):
        self.id = id
        self.dist = float('inf')
        self.prev = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in vertices}
        self.edge_weights = {}

    def connect(self, u, v, weight):
        self.adj_list[u].append(v)
        self.edge_weights[(u, v)] = weight

    def initialize(self, source):
        for vertex in self.vertices:
            vertex.dist = float('inf')
            vertex.prev = None
        source.dist = 0

    def relax(self, u, v):
        w = self.edge_weights[(u, v)]
        if v.dist > u.dist + w:
            v.dist = u.dist + w
            v.prev = u

    def bellman_ford(self, source):
        self.initialize(source)
        for _ in range(len(self.vertices) - 1):
            for (u, v) in self.edge_weights:
                self.relax(u, v)
        # Check for negative cycles
        for (u, v) in self.edge_weights:
            if v.dist > u.dist + self.edge_weights[(u, v)]:
                return False
        return True

if __name__ == '__main__':
    nodes = [Vertex(i) for i in range(5)]
    edges = [Edge(nodes[0], nodes[1], 6), Edge(nodes[0], nodes[3], 7),
             Edge(nodes[1], nodes[2], 5), Edge(nodes[1], nodes[3], 8),
             Edge(nodes[1], nodes[4], -4), Edge(nodes[2], nodes[1], -2),
             Edge(nodes[3], nodes[2], -3), Edge(nodes[3], nodes[4], 9),
             Edge(nodes[4], nodes[0], 2), Edge(nodes[4], nodes[2], 7)]

    g = Graph(nodes)
    for e in edges:
        g.connect(e.src, e.dest, e.cost)

    print(g.bellman_ford(nodes[0]))
