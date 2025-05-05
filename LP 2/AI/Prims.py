import heapq

def prim_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]  # (cost, vertex)
    total_cost = 0
    mst_edges = []

    while min_heap:
        cost, current = heapq.heappop(min_heap)
        if current in visited:
            continue

        visited.add(current)
        total_cost += cost
        if cost != 0:
            mst_edges.append((prev_node, current, cost))

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor))
                node_info[neighbor] = current  # track previous

        prev_node = current

    return total_cost, mst_edges


# User Input Graph
def get_graph_input():
    n = int(input("Enter number of vertices: "))
    graph = {}
    print("Enter names of vertices (e.g., A B C):")
    vertices = []
    for _ in range(n):
        v = input("Vertex name: ").strip().upper()
        graph[v] = []
        vertices.append(v)

    e = int(input("Enter number of edges: "))
    print("Enter each edge as: vertex1 vertex2 weight (e.g., A B 5):")
    for _ in range(e):
        u, v, w = input().strip().upper().split()
        w = int(w)
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph, vertices


# Main
if __name__ == "__main__":
    graph, vertices = get_graph_input()
    node_info = {}
    start_node = input("Enter starting vertex: ").strip().upper()

    total_cost, mst_edges = prim_mst(graph, start_node)

    print("\nMinimum Spanning Tree edges:")
    for u, v, cost in mst_edges:
        print(f"{u} - {v} (Weight: {cost})")

    print(f"Total cost of MST: {total_cost}")
