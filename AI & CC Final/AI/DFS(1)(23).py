# Simple Recursive DFS on Undirected Graph

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

def main():
    graph = {}
    visited = set()

    edges = int(input("How many edges? "))

    for _ in range(edges):
        u, v = input("Enter edge (e.g. A B): ").split()

        # Add edge both ways since the graph is undirected
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)

    start = input("Start DFS from node: ")

    print("DFS Traversal:")
    dfs(graph, start, visited)

if __name__ == "__main__":
    main()
