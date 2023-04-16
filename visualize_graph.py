import networkx as nx
import matplotlib.pyplot as plt
from model.Graph import Graph
from inputs.input_generation import generate_input_dict
from logger import Logger

def visualize_graph(graph: Graph, logger: Logger):
    # convert your graph to a networkx graph object
    nx_graph = nx.Graph(graph.nodeDict)

    # get positions for nodes to use for plotting
    pos = nx.spring_layout(nx_graph)

    # draw the networkx graph with matplotlib
    nx.draw(nx_graph, pos, with_labels=True, font_weight='bold')
    edge_labels = nx.get_edge_attributes(nx_graph, 'weight')
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_color='red')
    # plt.show()
    plt.savefig(f'{logger.dir_path}/graph.png')


