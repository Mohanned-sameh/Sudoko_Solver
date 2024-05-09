#!/usr/bin/env python3
import random


def printSolution(board):
    """A utility function to print the solution"""
    for row in board:
        print(" ".join(map(str, row)))


def isSafe(board, row, col, num):
    """Check whether it will be legal to assign num to the given row, col"""
    n = len(board)
    sqrt_n = int(n**0.5)

    # Check row and column for duplicates
    for x in range(n):
        if board[row][x] == num or board[x][col] == num:
            return False

    # Check subgrid for duplicates
    startRow = row - row % sqrt_n
    startCol = col - col % sqrt_n
    for i in range(sqrt_n):
        for j in range(sqrt_n):
            if board[i + startRow][j + startCol] == num:
                return False
    return True


def solveSudoku(board, row, col):
    """Takes a partially filled-in grid and attempts to assign values to all
    unassigned locations in such a way to meet the requirements for
    Sudoku solution (non-duplication across rows, columns, and boxes)"""
    n = len(board)
    if row == n:
        return True

    if col == n:
        return solveSudoku(board, row + 1, 0)

    if board[row][col] > 0:
        return solveSudoku(board, row, col + 1)

    nums = random.sample(range(1, n + 1), n)
    for num in nums:
        if isSafe(board, row, col, num):
            board[row][col] = num
            if solveSudoku(board, row, col + 1):
                return True
        board[row][col] = 0
    return False


def generateRandomBoard(N):
    """Generate a random valid Sudoku board"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solveSudoku(board, 0, 0)
    return board


if __name__ == "__main__":
    """Main function to test above functions"""
    N = int(input("Enter the size of the Sudoku board (N x N): "))
    if N <= 0:
        print("N should be greater than 0")
        exit(1)
    elif N % int(N**0.5) != 0:
        print("N should be a perfect square")
        exit(1)
    board = generateRandomBoard(N)
    printSolution(board)
