# Sudoku Solver

This Python script generates a random valid Sudoku board and solves it using backtracking.

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the script file `sudoku_solver.py`.
2. Run the script using the following command:
   `python sudoku_solver.py`
3. The script will generate a random Sudoku board and print the solution.

## How it Works

- The script implements backtracking to solve the Sudoku puzzle.
- It starts from an empty Sudoku grid and recursively tries to assign numbers to empty cells while ensuring that the assignment is valid according to Sudoku rules.
- If a solution is found, it prints the solution.
