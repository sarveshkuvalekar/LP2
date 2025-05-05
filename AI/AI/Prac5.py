import heapq

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

def prims_mst(graph, start):
    visited = set()                    # Stores nodes already in MST
    min_heap = [(0, start)]            # Priority queue: (edge cost, node)
    total_cost = 0                     # Total weight of MST

    while min_heap:
        cost, u = heapq.heappop(min_heap)  # Get node with minimum edge
        if u not in visited:
            visited.add(u)            # Add node to MST
            total_cost += cost        # Add cost to total
            for v, weight in graph[u]:  # Explore neighbors
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))  # Push edge

    return total_cost


# Run Prim's algorithm from vertex 'A'
print("Total cost of MST:", prims_mst(graph, 'A'))