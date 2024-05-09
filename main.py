#!/usr/bin/env python3
import random

N = 9


def printSolution(board):
    """A utility function to print the solution"""
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col, num):
    """Check whether it will be legal to assign num to the given row, col"""
    for x in range(N):
        if board[row][x] == num:
            return False

    for x in range(N):
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

    nums = random.sample(range(1, N + 1), N)
    for num in nums:
        if isSafe(board, row, col, num):
            board[row][col] = num
            if solveSudoku(board, row, col + 1):
                return True
        board[row][col] = 0
    return False


def generateRandomBoard():
    """Generate a random valid Sudoku board"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solveSudoku(board, 0, 0)
    return board


if __name__ == "__main__":
    """Main function to test above functions"""
    board = generateRandomBoard()
    print("Randomly generated Sudoku board:")
    printSolution(board)
