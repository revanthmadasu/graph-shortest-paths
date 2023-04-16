from inputs import cmd_inputs
from model.Graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
def main():
    # creating graph
    inputs = cmd_inputs()
    graph = Graph(inputs)
    
    # bfs traversal
    bfs(graph)

    # dijkstra algorithm
    dist, prev = dijkstra(graph, 1)
    print(dist)
    print(prev)

    # bellman ford algorithm
    dist_bell, prev_bell = bellman_ford(graph, 1)
    print(dist_bell)
    print(prev_bell)

main()
