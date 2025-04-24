import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {v: [] for v in vertices}
        self.weights = {}

    def add_edge(self, u, v, weight):
        self.edges[u].append(v)
        self.weights[(u, v)] = weight

    def dijkstra(self, start):
        start.dist = 0
        queue = [(0, start)]
        visited = set()

        while queue:
            _, u = heapq.heappop(queue)
            if u in visited:
                continue
            visited.add(u)

            for v in self.edges[u]:
                new_dist = u.dist + self.weights[(u, v)]
                if new_dist < v.dist:
                    v.dist = new_dist
                    v.prev = u
                    heapq.heappush(queue, (v.dist, v))

    def retrieve_path(self, v):
        path = []
        while v:
            path.append(v.id)
            v = v.prev
        return list(reversed(path))

class Node:
    def __init__(self, id):
        self.id = id
        self.dist = float('inf')
        self.prev = None
    def __lt__(self, other):
        return self.dist < other.dist

if __name__ == '__main__':
    nodes = [Node(i) for i in range(5)]
    g = Graph(nodes)
    connections = [(0, 1, 10), (0, 3, 5), (1, 2, 1), (1, 3, 2),
                   (2, 4, 4), (3, 1, 3), (3, 2, 9), (3, 4, 2),
                   (4, 0, 7), (4, 2, 6)]

    for u, v, w in connections:
        g.add_edge(nodes[u], nodes[v], w)

    g.dijkstra(nodes[0])
    print("Node | Distance | Path")
    for node in nodes:
        print(f"  {node.id}   |   {node.dist}    | {'->'.join(map(str, g.retrieve_path(node)))}")
