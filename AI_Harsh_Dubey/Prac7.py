def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]: return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]: return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]: return False
    return True

def solve(board, col, n):
    if col >= n: return True
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve(board, col + 1, n): return True
            board[row][col] = 0
    return False

def print_board(board):
    for row in board:
        print(' '.join('Q' if cell else '_' for cell in row))

def n_queens(n):
    board = [[0]*n for _ in range(n)]
    if solve(board, 0, n):
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    n = int(input("Enter number of queens: "))
    n_queens(n)