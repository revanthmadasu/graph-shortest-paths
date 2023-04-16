from model.Graph import Graph
def dijkstra(graph: Graph, source: int):
    Q = set()
    dist = {}
    prev = {}

    # Initialization
    for node in graph.get_nodes():
        dist[node] = float('inf')
        prev[node] = None
        Q.add(node)
    dist[source] = 0

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)

        for v in graph.get_neighbours(u):
            if v in Q:
                new_dist = dist[u] + graph.get_weight(u, v)
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
    return dist, prev