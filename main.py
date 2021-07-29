# Mohamad Darwiche
# Solving a Sudoku using Backtracking

# helper function
def valid_move(board, row, col, number):
    for x in range(9):
        if board[row][x] == number:
            return False
    for x in range(9):
        if board[x][col] == number:
            return False
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if board[corner_row + x][corner_col + y] == number:
                return False
    return True


def solve(board, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    if board[row][col] > 0:
        return solve(board, row, col + 1)

    for num in range(1, 10):
        if valid_move(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col + 1):
                return True
        board[row][col] = 0
    return False

# 0 means empty here
board = [[0, 3, 2, 9, 4, 0, 6, 0, 0],
         [5, 9, 0, 0, 0, 6, 7, 0, 0],
         [7, 0, 4, 0, 5, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 1, 0, 6, 0],
         [0, 0, 5, 7, 6, 0, 3, 4, 2],
         [6, 0, 3, 4, 0, 0, 0, 9, 0],
         [2, 0, 0, 1, 8, 9, 0, 7, 0],
         [0, 0, 9, 0, 0, 0, 8, 5, 1],
         [8, 0, 0, 0, 3, 4, 0, 2, 0]]

# Print results (solved puzzle)
if solve(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
else:
    print("Sorry. This sudoku has no solution.")
