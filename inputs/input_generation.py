import random

def generate_input_dict(num_nodes, directed=True, weighted=True, max_weight=10):
    input_dict = {'n': num_nodes, 'direction': 1 if directed else 0, 'weighted': weighted, 'edges': []}
    
    for i in range(1, num_nodes+1):
        for j in range(i+1, num_nodes+1):
            if random.random() < 0.3:
                if weighted:
                    weight = random.randint(1, max_weight)
                    input_dict['edges'].append((i, j, weight))
                else:
                    input_dict['edges'].append((i, j))
                if not directed:
                    if weighted:
                        input_dict['edges'].append((j, i, weight))
                    else:
                        input_dict['edges'].append((j, i))
    return input_dict

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

input_dict = generate_input_dict(num_nodes=25, directed=False, weighted=True, max_weight=100)
print(input_dict)