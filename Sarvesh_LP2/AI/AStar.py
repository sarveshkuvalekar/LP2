import heapq

# Goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Helper function to flatten state for easy comparison
def flatten(state):
    return tuple(item for row in state for item in row)

# Heuristic: Number of misplaced tiles
def heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Find the position of 0 (blank)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Move the blank in a direction
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # U, D, L, R

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star(start):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))  # (f = h + g, g, state, path)

    while pq:
        f, g, current, path = heapq.heappop(pq)
        state_id = flatten(current)

        if current == goal_state:
            print("Goal state reached!")
            print("Total moves:", len(path))
            return path + [current]

        if state_id in visited:
            continue

        visited.add(state_id)

        for neighbor in get_neighbors(current):
            heapq.heappush(pq, (g + 1 + heuristic(neighbor), g + 1, neighbor, path + [current]))

    return None

# Function to print the state
def print_state(state):
    for row in state:
        print(row)
    print("------")

# Initial state for the puzzle
initial_state = [[1, 2, 3],
                 [4, 0, 6],
                 [7, 5, 8]]

# Print the initial state
print("Initial State:")
print_state(initial_state)

# Solve the puzzle
solution_path = a_star(initial_state)

if solution_path:
    print("Solved path:")
    for step in solution_path:
        print_state(step)
else:
    print("No solution found.")
