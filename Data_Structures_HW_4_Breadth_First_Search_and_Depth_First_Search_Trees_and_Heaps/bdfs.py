'''
Cole Johnson 2/29
For CS240
'''

# class to store key, data, and neighbor node array
class Node:
    def __init__(self, key, data, neighbor = []):
        self.key = key
        self.data = data
        self.neighbor = neighbor
    def __str__(self):
        return self.key

# class to store functions for bfs or dfs
class BDFS:
    def __init__(self, type):
        self.graph = []
        # type == BFS s.type == 0
        # type == DFS s.type == 1
        self.type = 0
        if type == 'DFS':
            self.type = 1
    
    # function to add a base node to the graph
    # queue type / fifo for adding base nodes
    def add(self, node):
        self.graph.append(node)

    # creates a new graph array by adding the first nodes neighbors to the graph array
    # in BFS the neighbor nodes are added to the end
    # in DFS the neighbor nodes are added to the front
    def __append_neighbors__(self, graph):
        if not self.type: # BFS mode
            # add neighbor array to the end of graph array
            for neighbor in graph[0].neighbor:
                graph.append(neighbor)
            graph.pop(0)
        else: # DFS mode
            # add the graph to the end of neighbor array and return neighbor array
            if graph:
                old_graph = graph[:] # shallow copy of graph
                graph = graph[0].neighbor[:] # shallow copy of neighbor
                old_graph.pop(0)
                # first node has no neighbors
                if not graph:
                    return old_graph
                # if neighbors exist
                for node in old_graph:
                    graph.append(node)
            else:
                graph = None
        return graph
    
    # returns the data of a specific node from its key
    def search_via_key(self, key):
        graph = self.graph[:] # create shallow copy
        while graph:
            if graph[0].key == key:
                return graph[0].data
            graph = self.__append_neighbors__(graph)
        return None

    # returns the key of a specific node from its data
    def search_via_data(self, data):
        graph = self.graph[:] # create shallow copy
        while graph:
            if graph[0].data == data:
                return graph[0].key
            graph = self.__append_neighbors__(graph)
        return None

    # returns the key found after a given number of moves through the graph array in BFS or DFS mode
    def pop_after_moves(self, moves):
        graph = self.graph[:]
        for x in range(moves):
            if graph:
                graph = self.__append_neighbors__(graph)
        if graph:
            return graph.pop(0)
        return None

# creating the class
bfs = BDFS('BFS')
dfs = BDFS('DFS')
# creating p nodes
p5 = Node("p5", 5)
p3 = Node("p3", 3)
p4 = Node("p4", 4, [p5])
p1 = Node("p1", 1, [p3, p4])
p2 = Node("p2", 2)
# add root p nodes to the class graphs
bfs.add(p1)
bfs.add(p2)
dfs.add(p1)
dfs.add(p2)
# set the amount of moves and it will loop through the bfs and dfs graph for that long
moves = 5
for move in range(moves + 1):
    print(f"bfs after {move} moves: {bfs.pop_after_moves(move)}")
    print(f"dfs after {move} moves: {dfs.pop_after_moves(move)}")
    print() # new line