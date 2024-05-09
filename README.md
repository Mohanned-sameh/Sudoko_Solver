# Sudoko Solver

Sudoku Solver using Backtracking Algorithm
The algorithm is implemented using recursion
The algorithm is implemented using the following steps:

1. Find the first empty cell in the board
2. Check if the number can be placed in the cell
3. If the number can be placed, place the number in the cell
4. Repeat the above steps for the next cell
5. If the number cannot be placed, backtrack and try the next number
6. If all numbers are tried and none of them can be placed, backtrack to the previous cell
7. Repeat the above steps until all cells are filled
