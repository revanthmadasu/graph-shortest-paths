import random

# random input generator
def generate_input_dict(num_nodes, directed=True, weighted=True, max_weight=10, negative_weights = False):
    input_dict = {'n': num_nodes, 'direction': 1 if directed else 0, 'weighted': weighted, 'edges': []}
    
    for i in range(1, num_nodes+1):
        for j in range(i+1, num_nodes+1):
            # higher % of edges for lesser node to fully connect the graph
            if (random.random() < 0.3 and num_nodes > 15) or (num_nodes < 15 and random.random() < 0.5) or (num_nodes < 5 and random.random() < 0.9):
                if weighted:
                    weight = random.randint(1, max_weight)
                    if negative_weights:
                        # approximately 40% negative weights
                        if random.randint(1,5) < 3:
                            weight *= -1
        
                    input_dict['edges'].append((i, j, weight))
                else:
                    input_dict['edges'].append((i, j))
                if not directed:
                    if weighted:
                        input_dict['edges'].append((j, i, weight))
                    else:
                        input_dict['edges'].append((j, i))
    return input_dict

# custom user input from cmd
def cmd_inputs() -> dict:
    weighted = input("Is it a weighted graph: \ny/N").upper() == 'Y'
    direction = input("Select direction: \n1 for Undirected graph \n2 for Directed graph ")
    n, e = map(int, input("Enter number of vertices and edges ").split(" "))
    edges = []
    print("Enter edges")
    for i_e in range(e):
        if weighted:
            v1, v2, w = map(int, input().split(" "))
            edges.append((v1, v2, w))
        else:
            v1, v2 = map(int, input().split(" "))
            edges.append((v1, v2))
    return {'n': n, 'e': e, 'edges': edges, 'direction': direction, 'weighted': weighted}
