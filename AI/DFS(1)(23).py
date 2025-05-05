def dfs(graph, node, visited):
    print(node, end=' ')
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = {}
nodes = input("Enter all nodes: ").split()

for node in nodes:
    neighbors = input(f"Enter neighbors of {node}: ").split()
    graph[node] = neighbors

print(graph)

start = input("Enter starting node: ")
visited = set()

print("DFS Traversal:")
dfs(graph, start, visited)




# def dfs_stack(graph, start):
#     visited = set()
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             for neighbor in reversed(graph[node]):
#                 if neighbor not in visited:
#                     stack.append(neighbor)

# # Taking user input to build the graph
# graph = {}
# nodes = input("Enter all nodes (space-separated): ").split()

# for node in nodes:
#     neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
#     graph[node] = neighbors

# print("\nGraph representation:")
# print(graph)

# start = input("Enter starting node: ")

# print("\nDFS Traversal (using stack):")
# dfs_stack(graph, start)
