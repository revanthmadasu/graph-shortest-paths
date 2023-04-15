from inputs import cmd_inputs
from model.Graph import Graph
from algorithms.bfs import bfs
def main():
    inputs = cmd_inputs()
    graph = Graph(inputs)
    bfs(graph)

main()
