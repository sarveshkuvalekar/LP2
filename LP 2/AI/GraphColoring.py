# Function to check if assigning a color is valid
def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if assignment.get(neighbor) == color:
            return False
    return True

# Recursive backtracking function to assign colors
def graph_coloring(graph, colors, assignment, node_index=0):
    nodes = list(graph.keys())

    if node_index == len(nodes):
        return True  # All nodes colored successfully

    node = nodes[node_index]

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            if graph_coloring(graph, colors, assignment, node_index + 1):
                return True
            del assignment[node]  # backtrack

    return False

# User input for graph
def get_user_graph():
    n = int(input("Enter number of vertices: "))
    graph = {}
    print("Enter the name of each vertex (e.g., A, B, C):")
    vertices = []
    for _ in range(n):
        v = input("Vertex name: ").strip().upper()
        vertices.append(v)
        graph[v] = []

    e = int(input("Enter number of edges: "))
    print("Enter each edge as two space-separated vertex names (e.g., A B):")
    for _ in range(e):
        u, v = input("Edge: ").strip().upper().split()
        if u in graph and v in graph:
            graph[u].append(v)
            graph[v].append(u)
        else:
            print("Invalid vertices. Please re-enter this edge.")
    
    return graph, vertices

# Main driver
if __name__ == "__main__":
    graph, vertices = get_user_graph()

    k = int(input("Enter number of colors available: "))
    colors = []
    print("Enter the color names:")
    for _ in range(k):
        colors.append(input("Color: ").strip().capitalize())

    assignment = {}
    if graph_coloring(graph, colors, assignment):
        print("\nColoring solution found:")
        for node in vertices:
            print(f"{node}: {assignment[node]}")
    else:
        print("No valid coloring possible with given colors.")
