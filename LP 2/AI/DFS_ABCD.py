# Function to create a graph with letter-labeled vertices
def create_graph():
    n = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))

    # Automatically assign vertex labels from A, B, C, ...
    labels = [chr(65 + i) for i in range(n)]  # 65 = ASCII for 'A'
    graph = {label: [] for label in labels}

    print("Vertex labels:", labels)
    print("Enter each edge as two space-separated vertex labels (e.g., A B):")
    for _ in range(e):
        u, v = input().split()
        if u not in graph or v not in graph:
            raise ValueError("Invalid edge: vertices must be among " + str(labels))
        graph[u].append(v)
        graph[v].append(u)

    return graph, labels

# Recursive DFS
def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# Main
if __name__ == "__main__":
    graph, labels = create_graph()

    print("\nDFS Traversal starting from vertex A:")
    visited_dfs = {label: False for label in labels}
    dfs(graph, 'A', visited_dfs)
