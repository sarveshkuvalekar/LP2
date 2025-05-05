def isSafe(node, graph, color, colors):
    for adj in range(len(graph)):
        if graph[node][adj] == 1 and colors[adj] == color:
            return False
    return True

def graphColoring(graph, m, colors, node):
    if node == len(graph):
        return True  # All nodes colored

    for clr in range(1, m + 1):
        if isSafe(node, graph, clr, colors):
            colors[node] = clr
            if graphColoring(graph, m, colors, node + 1):
                return True
            colors[node] = 0  # Backtrack

    return False

# Input part
n = int(input("Enter number of vertices: "))  # Example: 4
graph = []
print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))  # Example 4x4 matrix

m = int(input("Enter number of colors: "))  # Example: 3
colors = [0] * n

if graphColoring(graph, m, colors, 0):
    print("Colors assigned to vertices:")
    print(colors)
else:
    print("No solution found.")
