def is_safe(graph, color, c, v):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True  # All vertices are assigned

    for c in range(1, m + 1):
        if is_safe(graph, color, c, v):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0  # Backtrack
    return False

def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n

    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist.")
        return False

    print("Color assignment to vertices:")
    for i in range(n):
        print(f"Vertex {i + 1} --> Color {color[i]}")
    return True

# Example Graph (Adjacency Matrix)
# 4 vertices and edges between (0-1), (0-2), (1-2), (1-3)
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

m = 3  # Number of colors
graph_coloring(graph, m)