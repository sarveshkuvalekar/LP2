from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
queue = deque()

def bfs_recursive():
    if not queue:
        return

    current = queue.popleft()
    print(current)
    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    bfs_recursive()

# Start from 'A'
queue.append('A')
print("Breadth First Search traversal starting from A:")
bfs_recursive()
