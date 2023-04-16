from inputs.input_generation import cmd_inputs
from inputs.input_generation import generate_input_dict
from model.Graph import Graph
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra
from algorithms.bellman_ford import bellman_ford
from visualize_graph import visualize_graph
from logger import Logger
import sys
# analyses algorithm on different data sizes and logs results
def analyseAlgorithm(logger: Logger, alg, displayAlg):
    nodes_sizes = [10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000]
    # nodes_sizes = [10, 25, 50, 75]
    runtimes = []
    for size in nodes_sizes:
        input_dict = generate_input_dict(num_nodes=size, directed=False, weighted=True, max_weight=1000, negative_weights= False)
        graph = Graph(input_dict)
        runtime = alg(graph)['runtime']
        runtimes.append(runtime)
    logger.logAnalyseRuntimes(runtimes, displayAlg)

def main(args):

    # Logger to save outputs
    logger = Logger()
    logger.start()

    # creating graph
    # get input from command line
    if 'cmd_input' in args:
        input_dict = cmd_inputs()
    else:
        input_dict = generate_input_dict(num_nodes=500, directed=False, weighted=True, max_weight=1000, negative_weights= False)

    logger.logInput(input_dict)

    graph = Graph(input_dict)
    visualize_graph(graph, logger)

    # bfs traversal
    if ('bfs' in args):
        bfs_res = bfs(graph)
        logger.logBfsOutput(bfs_res)

    # dijkstra algorithm
    if 'dijkstra' in args:
        dij_res = dijkstra(graph, 1)
        logger.logDijkstraOutput(dij_res)


    # bellman ford algorithm
    if 'bellman_ford' in args:
        bell_res = bellman_ford(graph, 1)
        logger.logBellmanOutput(bell_res)

    # compare runtimes
    if len(args) == 3:
        logger.logShortestPathRuntimes(dijkstra_result=dij_res, bellman_result=bell_res)
        logger.logAllRuntimes(bfs_result= bfs_res, dijkstra_result=dij_res, bellman_result=bell_res)

    # complete analysis
    if 'bfs' in args:
        analyseAlgorithm(logger, bfs, "bfs")

    if 'dijkstra' in args:
        analyseAlgorithm(logger, dijkstra, "dijkstra")

    if 'bellman_ford' in args:
        analyseAlgorithm(logger, bellman_ford, "bellman ford")

    logger.stop()

if len(sys.argv) == 1:
    main(['bfs', 'dijkstra', 'bellman_ford'])
else:
    main(sys.argv[1:])
