class Edge:
    def __init__(self, frm, to, cost):
        self.frm = frm
        self.to = to
        self.cost = cost

class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.previous = None

def relax(u, v, weight):
    if v.distance > u.distance + weight:
        v.distance = u.distance + weight
        v.previous = u

def initialize_vertices(network, source):
    for vertex in network.vertices:
        vertex.distance = float('inf')
        vertex.previous = None
    source.distance = 0

def bellman_ford(network, source):
    initialize_vertices(network, source)
    for _ in range(len(network.vertices) - 1):
        for (u, v) in network.edge_weights:
            relax(u, v, network.edge_weights[(u, v)])
    for (u, v) in network.edge_weights:
        if v.distance > u.distance + network.edge_weights[(u, v)]:
            return False
    return True

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {}
        self.edge_weights = {}
        for vertex in vertices:
            self.edges[vertex] = []

    def add_edge(self, u, v, cost):
        self.edges[u].append(v)
        self.edge_weights[(u, v)] = cost

if __name__ == "__main__":
    # s=0, t=1, x=2, y=3, z=4
    vertices = [Vertex(i) for i in range(5)]
    edge_list = [
        Edge(vertices[0], vertices[1], 6),
        Edge(vertices[0], vertices[3], 7),
        Edge(vertices[1], vertices[2], 5),
        Edge(vertices[1], vertices[3], 8),
        Edge(vertices[1], vertices[4], -4),
        Edge(vertices[2], vertices[1], -2),
        Edge(vertices[3], vertices[2], -3),
        Edge(vertices[3], vertices[4], 9),
        Edge(vertices[4], vertices[0], 2),
        Edge(vertices[4], vertices[2], 7),
    ]

    graph = Graph(vertices)
    for edge in edge_list:
        graph.add_edge(edge.frm, edge.to, edge.cost)

    result = bellman_ford(graph, vertices[0])
    print("Negative-weight cycle found?" if not result else "No negative-weight cycle.")

    for v in vertices:
        pred = v.previous.label if v.previous else None
        print(f"Vertex {v.label}: Distance = {v.distance}, Predecessor = {pred}")
