# Function to create a graph
def create_graph():
    n = int(input("Enter the number of vertices: "))
    e = int(input("Enter the number of edges: "))
    graph = {i: [] for i in range(n)}

    print("Enter each edge as two space-separated vertex numbers (e.g., 0 1):")
    for _ in range(e):
        u, v = map(int, input().split())
        if u >= n or v >= n or u < 0 or v < 0:
            raise ValueError(f"Invalid edge: vertices must be between 0 and {n - 1}")
        graph[u].append(v)
        graph[v].append(u)

    return graph, n

# BFS using queue
def bfs(graph, start):
    from collections import deque
    visited = [False] * len(graph)
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
    graph, n = create_graph()

    print("\n\nBFS Traversal starting from node 0:")
    bfs(graph, 0)