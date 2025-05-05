# Take user input for size
n = int(input("Enter number of queens (n): "))
a = [[0]*n for _ in range(n)]
b = {}

def isColumnSafe(r, c):
    return all(a[i][c] == 0 for i in range(r))

def isLeftDiagonalSafe(r, c):
    i, j = r-1, c-1
    while i >= 0 and j >= 0:
        if a[i][j] == 1:
            return False
        i -= 1
        j -= 1
    return True

def isRightDiagonalSafe(r, c):
    i, j = r-1, c+1
    while i >= 0 and j < n:
        if a[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def isSafe(r, c):
    return isColumnSafe(r, c) and isLeftDiagonalSafe(r, c) and isRightDiagonalSafe(r, c)

def chessboard(r, c):
    if r >= n:
        return True  # found one solution
    while c < n:
        if isSafe(r, c):
            a[r][c] = 1
            b[r] = c
            if chessboard(r + 1, 0):
                return True
            # backtrack
            a[r][c] = 0
            del b[r]
        c += 1
    return False

chessboard(0, 0)

# Print the matrix
print("\nFinal Board:")
for row in a:
    print(" ".join("Q" if col else "." for col in row))

print("\nQueen positions (row: column):", b)
