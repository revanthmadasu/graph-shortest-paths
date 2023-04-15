def cmd_inputs() -> dict:
    direction = input("Select direction: \n1 for Undirected graph \n2 for Directed graph ")
    n, e = map(int, input("Enter number of vertices and edges ").split(" "))
    edges = []
    print("Enter edges")
    for i_e in range(e):
        v1, v2 = map(int, input().split(" "))
        edges.append((v1, v2))
    return {'n': n, 'e': e, 'edges': edges, 'direction': direction}
