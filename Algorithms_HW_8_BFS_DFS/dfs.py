'''
Cole Johnson 3/4
For CS240
'''
# solving a maze with dfs
'''
i thought that a dfs would be best for solving the maze as you want to test each action before testing the next
action.
'''

# ==================== functions ==================== #

# function to check for valid action that is within bounds of the maze
def valid(x, y) -> bool:
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0

# recursive program to solve the maze
# moves through the maze and returns a solution path
def dfs(x, y, path, end, maze):
    # base case of path not working
    if x == end[0] and y == end[1]:
        return path + [(x, y)]
    # if in a valid position
    if valid(x, y):
        maze[x][y] = -1  # mark the current cell as visited
        # try moving in different directions (up, down, left, right)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            # split into multiple paths
            new_path = dfs(new_x, new_y, path + [(x, y)], end, maze)
            if new_path:
                return new_path
        maze[x][y] = 0  # Unmark the cell if no valid path is found
    return None

# function to call the recursive function that solve the maze
def solve_maze(maze, start, end):
    s_x, s_y = start
    solution = dfs(s_x, s_y, [], end, maze)
    return solution

# ==================== main code ==================== #

# example maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0]
]
# start and end positions
start = (0, 0)
end = (4, 2)

# solving the maze
solution = solve_maze(maze, start, end)

# print solution
if solution:
    print("Solution found:")
    for s in solution:
        print(s)
else:
    print("No solution found.")