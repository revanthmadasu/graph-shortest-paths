from model.Graph import Graph
import time
def bfs(graph: Graph, source=1):
    start_time = time.time()

    visited = set()
    # print(f'Starting bfs traversal with {source}')
    queue = [source]

    # starting traversal
    while len(queue) != 0:
        cur_node = queue[0]
        if cur_node in visited:
            # print(f"{cur_node} already visited.")
            queue.remove(cur_node)
            continue
        # print(f'Visiting {cur_node}')
        visited.add(cur_node)

        queue.extend(graph.get_neighbours(cur_node))
        queue.remove(cur_node)
    end_time = time.time()
    run_time = end_time - start_time
    print("BFS runtime: ", run_time, "seconds")
    return run_time
    # print("Traversal done")