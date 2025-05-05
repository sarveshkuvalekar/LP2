
def prim_mst(graph, n):
    keys = [float('inf')] * n
    parent = [-1] * n
    keys[0] = 0
    mst_set = [False] * n

    for _ in range(n):
        u = min((keys[i], i) for i in range(n) if not mst_set[i])[1]
        mst_set[u] = True

        for v in range(n):
            if graph[u][v] and not mst_set[v] and graph[u][v] < keys[v]:
                keys[v] = graph[u][v]
                parent[v] = u

    # Calculate the sum of MST weights
    total_weight = 0
    print("Edge \tWeight")
    for i in range(1, n):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
        total_weight += graph[i][parent[i]]

    return total_weight

# Input and Example
n = int(input("Enter number of vertices: "))
print("Enter the adjacency matrix:")
graph = [list(map(int, input().split())) for _ in range(n)]
total_weight = prim_mst(graph, n)
print("Total weight of MST:", total_weight)
