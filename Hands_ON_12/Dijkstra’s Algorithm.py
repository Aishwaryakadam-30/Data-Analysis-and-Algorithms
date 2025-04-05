class Link:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight

class Node:
    def __init__(self, id):
        self.id = id
        self.cost = float('inf')
        self.parent = None

def update_path(u, v, weight):
    if v.cost > u.cost + weight:
        v.cost = u.cost + weight
        v.parent = u

def initialize(graph, source):
    for n in graph.nodes:
        n.cost = float('inf')
        n.parent = None
    source.cost = 0

def pick_min(queue):
    lowest = queue[0]
    for node in queue:
        if node.cost < lowest.cost:
            lowest = node
    queue.remove(lowest)
    return lowest

def dijkstra(graph, source):
    initialize(graph, source)
    processed = []
    queue = graph.nodes[:]
    while queue:
        u = pick_min(queue)
        processed.append(u)
        for neighbor in graph.neighbors[u]:
            update_path(u, neighbor, graph.edge_weights[(u, neighbor)])
    return processed

def build_path(end_node):
    route = []
    current = end_node
    while current:
        route.append(current.id)
        current = current.parent
    return route[::-1]

class DirectedGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.neighbors = {}
        self.edge_weights = {}
        for node in nodes:
            self.neighbors[node] = []

    def connect(self, u, v, cost):
        self.neighbors[u].append(v)
        self.edge_weights[(u, v)] = cost

if __name__ == "__main__":
    nodes = [Node(i) for i in range(5)]
    links = [
        Link(nodes[0], nodes[1], 10),
        Link(nodes[0], nodes[3], 5),
        Link(nodes[1], nodes[2], 1),
        Link(nodes[1], nodes[3], 2),
        Link(nodes[2], nodes[4], 4),
        Link(nodes[3], nodes[1], 3),
        Link(nodes[3], nodes[2], 9),
        Link(nodes[3], nodes[4], 2),
        Link(nodes[4], nodes[0], 7),
        Link(nodes[4], nodes[2], 6),
    ]

    g = DirectedGraph(nodes)
    for l in links:
        g.connect(l.source, l.dest, l.weight)

    result = dijkstra(g, nodes[0])

    print("Node | Cost | Path")
    for node in result:
        print(f"{node.id}    | {node.cost}   | {' -> '.join(map(str, build_path(node)))}")
