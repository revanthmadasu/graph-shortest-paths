from model.Graph import Graph
import time
def dijkstra(graph: Graph, source = 1):

    start_time = time.time()

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
    end_time = time.time()
    run_time = end_time - start_time
    print("Dijkstra runtime: ", run_time, "seconds")
    return {'dist': dist, 'prev': prev, 'runtime': run_time}