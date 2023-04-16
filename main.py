from inputs.input_generation import cmd_inputs
from inputs.input_generation import generate_input_dict
from model.Graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from visualize_graph import visualize_graph
def main():
    # creating graph
    # inputs = cmd_inputs()
    input_dict = generate_input_dict(num_nodes=1000, directed=False, weighted=True, max_weight=1000)
    graph = Graph(input_dict)
    # visualize_graph(graph)
    # bfs traversal
    bfs(graph)

    # dijkstra algorithm
    dist, prev = dijkstra(graph, 1)
    # print(dist)
    # print(prev)

    # bellman ford algorithm
    dist_bell, prev_bell = bellman_ford(graph, 1)
    # print(dist_bell)
    # print(prev_bell)

main()
