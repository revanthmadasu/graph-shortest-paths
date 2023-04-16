from collections import defaultdict


class Graph:
    def __init__(self, inputDict=None) -> None:
        self.nodeDict = defaultdict(lambda: None)
        if inputDict:
            self.type = 'undirected' if inputDict['direction'] == 1 else 'directed'
            self.weighted = inputDict['weighted']
            self.weightDict = defaultdict(lambda: None)

            # adding nodes
            for i_n in range(1, inputDict['n']+1):
                self.add_node(i_n)
            # connecting nodes
            for edge in inputDict['edges']:
                if self.weighted:
                    v1, v2, w = edge
                    self.connect_nodes(v1, v2, w)
                # for unweighted graph, default cost would be 1
                else:
                    v1, v2 = edge
                    self.connect_nodes(v1, v2)

    def add_node(self, val) -> None:
        self.nodeDict[val] = []
        self.weightDict[val] = defaultdict(lambda: None)

    def add_weight(self, val1, val2, weight):
        self.weightDict[val1][val2] = weight
        if self.type == 'undirected':
            self.weightDict[val2][val1] = weight


    def connect_nodes(self, val1, val2, weight=1) -> None:
        if val2 not in self.nodeDict[val1]:
            self.nodeDict[val1].append(val2)
            self.add_weight(val1, val2, weight)
        if self.type == 'undirected' and val1 not in self.nodeDict[val2]:
            self.nodeDict[val2].append(val1)
            self.add_weight(val2, val1, weight)

    def disconnect_nodes(self, val1, val2) -> None:
        if val2 in self.nodeDict[val1]:
            self.nodeDict[val1].remove(val2)
        if self.type == 'undirected' and val1 in self.nodeDict[val2]:
            self.nodeDict[val2].remove(val1)

    def is_connected(self, val1, val2) -> bool:
        return val1 in self.nodeDict[val2]
    
    def get_nodes(self) -> set:
        return self.nodeDict.keys()
    
    def get_neighbours(self, val):
        return self.nodeDict[val]
    
    def get_weight(self, val1, val2):
        return self.weightDict[val1][val2]