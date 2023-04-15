from model.Graph import Graph
def bfs(graph: Graph, source=-1):
    nodes = list(graph.get_nodes())
    if source == -1:
        source = sorted(nodes)[0]
    visited = set()
    print(f'Starting bfs traversal with {source}')
    queue = [source]

    # starting traversal
    while len(queue) != 0:
        cur_node = queue[0]
        if cur_node in visited:
            print(f"{cur_node} already visited.")
            queue.remove(cur_node)
            continue
        print(f'Visiting {cur_node}')
        visited.add(cur_node)

        queue.extend(graph.get_neighbours(cur_node))
        queue.remove(cur_node)
    print("Traversal done")