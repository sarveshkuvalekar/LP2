from heapq import heappop, heappush

# Define grid size and goal
goal = (4, 4)  # Goal position

# Heuristic function: Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(start, goal):
    open_list = [(heuristic(start, goal), 0, start)]  # (f, g, position)
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, g, current = heappop(open_list)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Move directions
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < 5 and 0 <= neighbor[1] < 5:  # Check grid bounds
                tentative_g = g + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, goal)
                    heappush(open_list, (f, tentative_g, neighbor))
                    came_from[neighbor] = current

    return None  # No path found

# Example start and goal positions
start = (0, 0)
path = astar(start, goal)

# Output the path
if path:
    print("Path:", path)
else:
    print("No path found.")
