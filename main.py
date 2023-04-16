from inputs import cmd_inputs
from model.Graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
def main():
    inputs = cmd_inputs()
    graph = Graph(inputs)
    bfs(graph)
    dist, prev = dijkstra(graph, 1)
    print(dist)
    print(prev)

main()
