# Define the graph as an adjacency list (undirected graph)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Set to keep track of visited nodes
visited = set()

def dfs(node):
    if node not in visited:
        print(node)  # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

# Start DFS from node 'A'
print("Depth First Search traversal starting from A:")
dfs('A')
