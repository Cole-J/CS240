'''
Cole Johnson 3/6
For CS240
'''

# ==================== pseudo code ==================== #

'''
function def
    create a list of the visited vertices but do not populate

    create list to store edges

    get the start vertex

    while not all vertices have been visited

        for each vertex in the visited set (starts with just the start vertex)

            get the min edge weight from the edges between the current vertex and its neighbors
        
        if it has a minimum edge add it to the store edges list

        add current vertice to visited
        
    return the min edge list
'''

# ==================== function code ==================== #

# function to get the min span array
# array is populated with tuples of the (vertex, min neighbor, weight)
def prim(graph):
    # visited vertices set
    visited = set()
    # min span array def
    minimum_spanning_tree = []
    # start vertex def
    start_vertex = next(iter(graph))
    # add start vertex to visited vertex pre loop
    visited.add(start_vertex)
    # main loop
    while (len(visited) < len(graph)):
        # the min edge of the current iteration
        min_edge = None
        # for each visited vertex
        for vertex in visited:
            # for each vertex neighbor and neighbors weight
            for neighbor, weight in graph[vertex].items():
                # min_edge is equal to the connecting edge with the least weight
                if neighbor not in visited and (min_edge is None or weight < min_edge[2]):
                    min_edge = (vertex, neighbor, weight)
        # if a min edge was found
        if min_edge:
            # save
            minimum_spanning_tree.append((min_edge[0], min_edge[1], min_edge[2]))
            # set the neighbor as visited
            visited.add(min_edge[1])
    # return resulting array of tups
    return minimum_spanning_tree

# ==================== main code ==================== #

# base graph
graph = {
    'A': {'B': 5, 'D': 9, 'E': 2},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'D': 3},
    'D': {'A': 9, 'C': 3, 'E': 4},
    'E': {'A': 2, 'D': 4}
}

# get the min span tree / array
mst = prim(graph)

# print
for edge in mst:
    print(edge)