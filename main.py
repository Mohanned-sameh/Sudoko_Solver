#!/usr/bin/env python3
"""
Sudoku Solver using Backtracking Algorithm
"""
N = 9


def printSolution(board):
    """A utility function to print the solution"""
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col, num):
    """Check whether it will be legal to assign num to the given row, col"""
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True


def solveSudoku(board, row, col):
    """Takes a partially filled-in grid and attempts to assign values to all
    unassigned locations in such a way to meet the requirements for
    Sudoku solution (non-duplication across rows, columns, and boxes)"""
    if row == N - 1 and col == N:
        return True

    if col == N:
        row += 1
        col = 0

    if board[row][col] > 0:
        return solveSudoku(board, row, col + 1)

    for num in range(1, N + 1, 1):
        if isSafe(board, row, col, num):
            board[row][col] = num
            if solveSudoku(board, row, col + 1):
                return True
        board[row][col] = 0
    return False


if __name__ == "__main__":
    """Main function to test above functions"""
    board = [[0 for j in range(N)] for i in range(N)]
    board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 0, 0, 0, 6, 8],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    if solveSudoku(board, 0, 0):
        printSolution(board)
    else:
        print("No solution exists")
