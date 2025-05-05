# Function to create a graph with letter-labeled vertices
def create_graph():
    n = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))

    labels = [chr(65 + i) for i in range(n)]  # Create labels: A, B, C, ...
    graph = {label: [] for label in labels}

    print("Vertex labels:", labels)
    print("Enter each edge as two space-separated vertex labels (e.g., A B):")
    for _ in range(e):
        u, v = input().split()
        if u not in graph or v not in graph:
            raise ValueError(f"Invalid edge: vertices must be among {labels}")
        graph[u].append(v)
        graph[v].append(u)

    return graph, labels

# BFS using queue
def bfs(graph, start):
    from collections import deque
    visited = {v: False for v in graph}
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# Main
if __name__ == "__main__":
    graph, labels = create_graph()

    print("\nBFS Traversal starting from vertex A:")
    bfs(graph, 'A')
