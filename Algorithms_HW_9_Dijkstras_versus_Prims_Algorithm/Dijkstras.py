'''
Cole Johnson 3/6
For CS240
'''

# ==================== pseudo code ==================== #

'''
function, parameters are start vertex and the graph

    create a list of distances equal to the number of vertices in the graph

    set start distance to 0

    create an array of unvisited vertices to keep track

    while not all vertices have been checked

        current vertice is the min of the unvisited
        
        remove current vertice from unvisited

        for each neighbor in the current vertice

            get the distance from the current vertice to the neighbor vertice
            
            if the distance is less than the known distance set new distance to known distance
'''

# ==================== function code ==================== #

# function to create a list of distances from a start vertice
def dijkstra_algorithm(graph, start):
    # set each unexplored vertex to inf distance
    distances = {vertex: float('infinity') for vertex in graph}
    # the distance of the start is 0  as its the start
    distances[start] = 0
    # create a set to store unvisited
    unvisited = set(graph.keys())
    # loop for each vertice so that we can know all distances from start
    while unvisited:
        # current is the min of the previous
        # lambda is used to get the current distance
        current = min(unvisited, key = lambda vertex: distances[vertex])
        # remove the current from the unvisited
        unvisited.remove(current)
        # for each neighbor connected to the current vertex
        # calculate their distance and if its less than the known distance set the new distance to the known
        for neighbor, weight in graph[current].items():
            # find the distance
            distance = distances[current] + weight
            # compare to prev vertex distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    # return list of distances from start
    return distances

# ==================== main code ==================== #

# base graph
graph = {
    'A': {'B': 5, 'D': 9, 'E': 2},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'D': 3},
    'D': {'A': 9, 'C': 3, 'E': 4},
    'E': {'A': 2, 'D': 4}
}

# input parameters
start = 'A'
end = 'C'

# gets the shortest distance from start vertex to all other vertices
shortest_distances = dijkstra_algorithm(graph, start)

# check the distances for the end parameters distance
shortest_path = shortest_distances[end]

# print
print(f"distance from '{start}' to '{end}' is {shortest_path}")