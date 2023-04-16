from inputs.input_generation import cmd_inputs
from inputs.input_generation import generate_input_dict
from model.Graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from visualize_graph import visualize_graph
from logger import Logger

# analyses algorithm on different data sizes and logs results
def analyseAlgorithm(logger: Logger, alg, displayAlg):
    nodes_sizes = [10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000]
    runtimes = []
    for size in nodes_sizes:
        input_dict = generate_input_dict(num_nodes=size, directed=False, weighted=True, max_weight=1000, negative_weights= False)
        graph = Graph(input_dict)
        runtime = alg(graph)['runtime']
        runtimes.append(runtime)
    logger.logAnalyseRuntimes(runtimes, displayAlg)

def main():

    # Logger to save outputs
    logger = Logger()
    logger.start()

    # creating graph
    # get input from command line
    # input_dict = cmd_inputs()
    input_dict = generate_input_dict(num_nodes=1000, directed=False, weighted=True, max_weight=1000, negative_weights= False)

    logger.logInput(input_dict)

    graph = Graph(input_dict)
    visualize_graph(graph, logger)

    # bfs traversal
    bfs_res = bfs(graph)
    logger.logBfsOutput(bfs_res)

    # dijkstra algorithm
    dij_res = dijkstra(graph, 1)
    logger.logDijkstraOutput(dij_res)


    # bellman ford algorithm
    bell_res = bellman_ford(graph, 1)
    logger.logBellmanOutput(bell_res)

    # compare runtimes
    logger.logShortestPathRuntimes(dijkstra_result=dij_res, bellman_result=bell_res)
    logger.logAllRuntimes(bfs_result= bfs_res, dijkstra_result=dij_res, bellman_result=bell_res)

    # complete analysis
    analyseAlgorithm(logger, bfs, "bfs")
    analyseAlgorithm(logger, dijkstra, "dijkstra")
    analyseAlgorithm(logger, bellman_ford, "bellman ford")

    logger.stop()

main()

