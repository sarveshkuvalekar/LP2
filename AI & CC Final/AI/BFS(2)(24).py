from collections import deque

# Function to add an edge to the graph (undirected)
def add_edge(graph, u, v):
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

# BFS function
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Queue to explore nodes level by level

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")  # Process the node (print in this case)
            visited.add(node)  # Mark the node as visited

            # Enqueue all unvisited neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Main function to handle user input and start BFS
def main():
    graph = {}

    # Get user input for the number of edges
    edges = int(input("How many edges? "))

    # Add edges to the graph
    for _ in range(edges):
        u, v = input("Enter edge (e.g. A B): ").split()
        add_edge(graph, u, v)

    start = input("Start BFS from node: ")

    print("BFS Traversal:")
    bfs(graph, start)

if __name__ == "__main__":
    main()
