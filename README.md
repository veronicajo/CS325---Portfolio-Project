# Introduction
Portfolio Assignment for CS 325 Winter 2021

sudoku.py does the following:

Allows user to solve a Sudoku puzzle. There is only one puzzle available. Once the user completes the puzzle, the user's solution is verified and either shows that the user has solved the puzzle or that the user's solution is incorrect.

Verifies if a completed Sudoku puzzle was solved correctly or if it has not been solved. 

Finds a solution to a Sudoku puzzle and outputs the completed grid.


# Running the code
Enter the following line to the command terminal to run the program:

```
$ python3 sudoku.py
```

Follow the directions printed to the console.

# Requirements
All letters typed for the input must be capitalized.

>E.g. Type "A4" to specify a cell, not "a4."

The program is only ensured to work correctly with a standard size Sudoku grid, which is 9x9.

If supplying a Sudoku grid to verify or generate a solution, you must provide the values in each 3x3 grid in order from the top 3 3x3 grids (going left to right), middle 3 (going left to right), and bottom 3 (going left to right).

>E.g. the puzzle pictured [here](https://en.wikipedia.org/wiki/Sudoku#/media/File:Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg) would be inputted as: 
```
5 3 0 6 0 0 0 9 8 0 7 0 1 9 5 0 0 0 0 0 0 0 0 0 0 6 0 8 0 0 4 0 0 7 0 0 0 6 0 8 0 3 0 2 0 0 0 3 0 0 1 0 0 6 0 6 0 0 0 0 0 0 0 0 0 0 4 1 9 0 8 0 2 8 0 0 0 5 0 7 9
```

# When Testing the Code
If solving the Sudoku puzzle provided by the program, the solution is:
```
[
    [1, 5, 3, 9, 2, 8, 6, 4, 7],
    [8, 7, 2, 3, 4, 6, 1, 5, 9],
    [4, 9, 6, 5, 1, 7, 2, 8, 3],
    [3, 1, 4, 7, 9, 2, 8, 6, 5],
    [9, 6, 8, 5, 3, 4, 2, 1, 7],
    [7, 2, 5, 1, 6, 8, 3, 4, 9],
    [5, 7, 6, 2, 3, 1, 4, 8, 9],
    [4, 9, 1, 6, 8, 5, 7, 2, 3],
    [8, 3, 2, 9, 7, 4, 6, 5, 1]
]
```

Sample input for a correctly solved Sudoku puzzle:
```
1 9 6 5 3 4 7 2 8 2 5 3 8 1 7 4 6 9 8 7 4 2 9 6 3 5 1 8 5 3 9 6 2 4 7 1 1 9 4 3 7 8 6 2 5 6 2 7 4 1 5 9 8 3 6 8 5 3 1 9 2 4 7 7 4 2 5 8 6 9 3 1 1 3 9 7 4 2 5 6 8
```

Sample input for an incorrectly solved Sudoku puzzle:
```
1 9 6 5 3 4 7 2 8 2 5 3 8 1 7 4 6 9 1 7 4 2 9 6 3 5 1 8 5 3 9 6 2 4 7 1 1 9 4 3 7 8 6 2 5 6 3 7 4 1 5 9 8 3 6 8 5 3 1 9 2 4 7 7 4 2 5 8 6 9 3 1 1 3 9 7 4 2 5 6 9
```

Sample input of a Sudoku puzzle to generate a solution for is (this is the unsolved version of the sample input provided for a correctly solved grid):
```
1 9 0 0 3 0 0 2 0 0 0 0 8 0 7 0 6 0 0 0 4 0 0 0 0 0 0 0 0 0 0 0 2 4 7 0 0 0 0 0 0 0 0 0 5 0 0 7 0 0 5 9 0 3 6 0 0 3 0 0 0 0 0 0 4 0 0 8 0 9 0 0 0 0 0 0 4 0 5 0 0
```
