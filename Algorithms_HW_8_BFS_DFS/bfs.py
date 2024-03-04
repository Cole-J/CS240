'''
Cole Johnson 3/4
For CS240
'''
# finding the shortest path with a bfs
'''
i thought that this would be best for a bfs as you will have to check each neighbor and each neighbors neighbor.
'''

# ==================== functions ==================== #

# function to get the shortest path in a graph from a start and goal
def bfs_shortest_path(graph, start, goal):
    # Check if the start and goal nodes are valid
    if start not in graph or goal not in graph:
        # error
        print("Start or goal node not in the graph")
    # using a list as a queue to perform BFS
    # queue def
    queue = [(start, [start])]
    # save visited nodes
    visited = set()
    while queue:
        # current node def and current path def
        cn, path = queue.pop(0)
        # base case
        if cn == goal:
            return path  # Return the shortest path
        # if the current node is not in the visited set add it to the set
        if cn not in visited:
            visited.add(cn)
            # add neighbor nodes to the queue
            for neighbor in graph[cn]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

# ==================== main code ==================== #

# graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# start and goal node
start = 'A'
goal = 'H'

# get the shortest path
shortest_path = bfs_shortest_path(graph, start, goal)

# print the path
if shortest_path:
    print(f"path {shortest_path}")
else:
    print("no path")