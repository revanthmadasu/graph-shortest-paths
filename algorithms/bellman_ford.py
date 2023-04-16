from model.Graph import Graph
from typing import List, Tuple, Union
from collections import defaultdict


def bellman_ford(graph: Graph, source: int) -> Tuple[List[int], List[Union[int, None]]]:
    nodes = graph.get_nodes()
    edges = []
    for node in nodes:
        for neighbor in graph.get_neighbours(node):
            edges.append((node, neighbor, graph.get_weight(node, neighbor)))
    
    # Step 1: initialize graph
    distance = defaultdict(lambda: float('inf'))
    predecessor = defaultdict(lambda: None)
    distance[source] = 0
    
    # Step 2: relax edges repeatedly
    for i in range(len(nodes) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u
                
    # Step 3: check for negative-weight cycles
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    
    return [distance, predecessor]