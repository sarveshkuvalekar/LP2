from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft() 
        if node not in visited:
            print(node, end=' ') 
            visited.add(node)      
            
        
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {}
nodes = input("Enter all nodes : ").split()

for node in nodes:
    neighbors = input(f"Enter neighbors of {node} : ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")


print("BFS Traversal:")
bfs(graph, start)
