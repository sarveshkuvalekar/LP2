def is_safe(row, col, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup, n):
    if row_lookup[row] or slash_code_lookup[slash_code[row][col]] or backslash_code_lookup[backslash_code[row][col]]:
        return False
    return True


def solve_n_queens_util(board, col, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup, n, solutions):
    if col >= n:
        solutions.append(["".join(row) for row in board])
        return

    for i in range(n):
        if is_safe(i, col, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup, n):
            board[i][col] = 'Q'
            row_lookup[i] = True
            slash_code_lookup[slash_code[i][col]] = True
            backslash_code_lookup[backslash_code[i][col]] = True

            solve_n_queens_util(board, col + 1, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup, n, solutions)

            # Backtrack
            board[i][col] = '.'
            row_lookup[i] = False
            slash_code_lookup[slash_code[i][col]] = False
            backslash_code_lookup[backslash_code[i][col]] = False


def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Precompute diagonals
    slash_code = [[0 for _ in range(n)] for _ in range(n)]
    backslash_code = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            slash_code[r][c] = r + c
            backslash_code[r][c] = r - c + (n - 1)

    row_lookup = [False] * n
    slash_code_lookup = [False] * (2 * n - 1)
    backslash_code_lookup = [False] * (2 * n - 1)

    solutions = []
    solve_n_queens_util(board, 0, slash_code, backslash_code, row_lookup, slash_code_lookup, backslash_code_lookup, n, solutions)
    return solutions


# Main execution
if __name__ == "__main__":
    n = int(input("Enter the value of N for N-Queens: "))
    solutions = solve_n_queens(n)

    print(f"\nTotal Solutions: {len(solutions)}")
    for idx, solution in enumerate(solutions, 1):
        print(f"\nSolution #{idx}:")
        for row in solution:
            print(row)
