from inputs.input_generation import cmd_inputs
from inputs.input_generation import generate_input_dict
from model.Graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from visualize_graph import visualize_graph
from logger import Logger
def main():

    # Logger to save outputs
    logger = Logger()
    logger.start()

    # creating graph
    # get input from command line
    # input_dict = cmd_inputs()
    input_dict = generate_input_dict(num_nodes=100, directed=False, weighted=True, max_weight=1000, negative_weights= False)

    logger.logInput(input_dict)

    graph = Graph(input_dict)
    # visualize_graph(graph)

    # bfs traversal
    bfs(graph)

    # # dijkstra algorithm
    dij_res = dijkstra(graph, 1)
    logger.logDijkstraOutput(dij_res)


    # bellman ford algorithm
    bell_res = bellman_ford(graph, 1)
    logger.logBellmanOutput(bell_res)

    # compare runtimes
    logger.logRuntimes(dijkstra_result=dij_res, bellman_result=bell_res)
    logger.stop()

main()
