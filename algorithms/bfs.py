from model.Graph import Graph
from collections import deque
import time
def bfs(graph: Graph, source=1):
    start_time = time.time()

    visited = set()
    # print(f'Starting bfs traversal with {source}')
    queue = deque([source])
    prev = dict()

    # starting traversal
    while queue:
        cur_node = queue.popleft()
        if cur_node in visited:
            # print(f"{cur_node} already visited.")
            continue
        # print(f'Visiting {cur_node}')
        visited.add(cur_node)

        for neighbour in graph.get_neighbours(cur_node):
            if neighbour not in visited:
                queue.append(neighbour)
                prev[neighbour] = cur_node

    end_time = time.time()
    run_time = end_time - start_time
    print("BFS runtime: ", run_time, "seconds")
    return {'prev': prev, 'runtime': run_time}
    # print("Traversal done")