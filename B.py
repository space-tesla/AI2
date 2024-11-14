# Q.2 Write a Python program to implement the Depth First Search (DFS) algorithm. Refer to the following graph as input for the program. [Initial node = 1, Goal node = 7]

  1 → 3 → 5 → 7
  ↓ ↘ ↓ ↘
  2 → 4 → 6
Program:

# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [4],
    3: [4, 5],
    4: [6],
    5: [7],
    6: [7],
    7: []
}

# Depth First Search function
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  # Print the current node

    if start == goal:
        return True  # Goal node found

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

# Initialize DFS from node 1 to find node 7
print("DFS traversal path:")
dfs(graph, 1, 7)

Output:
DFS traversal path:
1 2 4 6 7
