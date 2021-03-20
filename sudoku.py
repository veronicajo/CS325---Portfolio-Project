from os import system, name

class SudokuPuzzle:
    """
    Can initialize a Sudoku puzzle for the user to solve, verify a completed Sudoku puzzle, and generate a solution to a Sudoku puzzle.
    """

    def __init__(self, board=None):
        """
        Initializes puzzle and decides which route to take depending on board input.
        """
        
        if board is not None: # a grid is specified to verify or generate solution
            if self.grid_done(board) is True:
                print(self.verify_solution(board))
            else:
                self.sudoku_solver(board)

        else: # initialize puzzle
            self._grid = [
                [1, " ", " ", 9, " ", " ", " ", 4, 7],
                [8, 7, 2, 3, " ", " ", " ", " ", 9],
                [" ", " ", 6, 5, " ", " ", " ", " ", " "],
                [3, " ", " ", " ", 9, " ", " ", 6, " "],
                [9, " ", " ", 5, " ", " ", " ", 1, " "],
                [" ", 2, " ", " ", " ", 8, " ", 4, " "],
                [" ", " ", 6, 2, " ", " ", " ", 8, " "],
                [4, " ", " ", " ", " ", 5, " ", " ", " "],
                [" ", 3, " ", 9, 7, " ", " ", " ", 1]
            ]
            # stores the starting values of the puzzle
            self._fixed = {
                "0": [0, 3, 7, 8],
                "1": [0, 1, 2, 3, 8],
                "2": [2, 3],
                "3": [0, 4, 7],
                "4": [0, 3, 7],
                "5": [1, 5, 7],
                "6": [2, 3, 7],
                "7": [0, 5],
                "8": [1, 3, 4, 8]
            }

            self.start()
    

    def print_grid(self, board):
        """
        Prints the current state of the grid.
        """

        # borders for the grid
        top_border = "╔═══╤═══╤═══╗╔═══╤═══╤═══╗╔═══╤═══╤═══╗"
        subset_border = "╠═══╪═══╪═══╣╠═══╪═══╪═══╣╠═══╪═══╪═══╣"
        bottom_border = "╚═══╧═══╧═══╝╚═══╧═══╧═══╝╚═══╧═══╧═══╝"
        cell_bottom = "╟───┼───┼───╢╟───┼───┼───╢╟───┼───┼───╢"

        row = 1
        label = 1
        while row < 10:
            count = 1
            while count < 10:
                if row == 1 and count == 1:
                    print("    A   B   C    D   E   F    G   H   I")
                    print("  " + top_border)
                
                if count == 3:
                    print("  " + subset_border)
                elif count > 1:
                    print("  " + cell_bottom)

                # printing the values in the grid
                print(
                    label, "║", board[row-1][count-1], "|", board[row-1][count], "|", board[row-1][count+1], "║"
                    "║", board[row][count-1], "|", board[row][count], "|", board[row][count+1], "║"
                    "║", board[row+1][count-1], "|", board[row+1][count], "|", board[row+1][count+1], "║"
                    )
                
                if row == 7 and count == 7:
                    print("  " + bottom_border, "\n")
                elif count == 7:
                    print("  " + subset_border)
                
                count += 3
                label += 1

            row += 3
    

    def start(self):
        """
        Displays puzzle rules and instructions to the user.
        Calls the prompt method to begin.
        """

        print("You cannot change the values the puzzle starts with. You can input a number from 1 to 9 into a valid cell by following the prompt instructions." + "\n")
        self.print_grid(self._grid)
        self.prompt()
    

    def prompt(self):
        """
        Prompts user to enter input and parses the input.
        """

        value = int(input("Please enter an integer from 1 to 9 to place in an empty cell: "))
        space = input("Please enter the cell to place the number, the letter must be capitalized (format example: A5): ")

        # dictionary to determine which cell to update in the grid
        space_conversion = {
            'A': [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]],
            'B': [[0, 1], [0, 4], [0, 7], [3, 1], [3, 4], [3, 7],[6, 1], [6, 4], [6, 7]],
            'C': [[0, 2], [0, 5], [0, 8], [3, 2], [3, 5], [3, 8], [6, 2], [6, 5], [6, 8]],
            'D': [[1, 0], [1, 3], [1, 6], [4, 0], [4, 3], [4, 6], [7, 0], [7, 3], [7, 6]],
            'E': [[1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7],[7, 1], [7, 4], [7, 7]],
            'F': [[1, 2], [1, 5], [1, 8], [4, 2], [4, 5], [4, 8], [7, 2], [7, 5], [7, 8]],
            'G': [[2, 0], [2, 3], [2, 6], [5, 0], [5, 3], [5, 6], [8, 0], [8, 3], [8, 6]],
            'H': [[2, 1], [2, 4], [2, 7], [5, 1], [5, 4], [5, 7],[8, 1], [8, 4], [8, 7]],
            'I': [[2, 2], [2, 5], [2, 8], [5, 2], [5, 5], [5, 8], [8, 2], [8, 5], [8, 8]]
        }

        space = space_conversion[space[0]][int(space[1])-1]
        box = space[0]
        cell = space[1]
        self.update_grid(box, cell, value)

        
    def update_grid(self, box, cell, value):
        """
        Determines if a move is valid and if it is, updates the grid.
        """

        # check if the move is valid
        if self.verify_move(box, cell, value) is True:
            self._grid[box][cell] = value
        else:
            print("\n" + "You can't update a starting cell and/or must enter a number from 1 to 9. Try again." + "\n")
            self.prompt()
        
        # clear console and print updated grid
        self.clear_screen()
        self.print_grid(self._grid)

        # check if the puzzle has been completed
        if self.grid_done(self._grid) is True:
            print("You've finished the puzzle! Now we'll check your answers." + "\n")
            print(self.verify_solution(self._grid), "\n")
        else:
            self.prompt()


    def grid_done(self, board):
        """
        Checks to see whether the grid has been completed.
        """

        # check to see if there is an empty cell in each 3x3 grid
        count = 0
        while count < 9:
            if " " in board[count]:
                return False
            else:
                count += 1
        
        return True
    

    def verify_move(self, box, cell, value):
        """
        Verifies whether attempted move is allowed.
        """

        # cell cannot be one of the starting values and must be a value from 1-9
        if cell not in self._fixed[str(box)] and value in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            return True
        else:
            return False
    

    def clear_screen(self):
        """
        Clears the console for next move.
        Method adapted from GeeksforGeeks.
        """

        if name == 'nt': # windows system
            _ = system('cls')
        else: # mac or linux system
            _ = system('clear')


    def verify_solution(self, board):
        """
        Verifies if the inputted solution is correct.
        """

        for i in range(9): # for each 3x3 grid
            for j in range(9): # for each value in 3x3 grid
                value = board[i][j]
                
                # check if value is distinct within 3x3 box
                box = board[i]
                if box.count(box[j]) > 1:
                    return("\n" + "Not solved, please try again.")
                
                # check if value is distinct in column
                if i in (0, 3, 6):
                    s = 0
                elif i in (1, 4, 7):
                    s = 1
                else:
                    s = 2

                while s < 9:
                    if j in (0, 3, 6):
                        t = 0
                    elif j in (1, 4, 7):
                        t = 1
                    else:
                        t = 2

                    while t < 9:
                        if board[s][t] == value and i != s and j != t:
                            return("\n" + "Not solved, please try again.")
                        t += 3
                    s += 3
                
                # check if value is distinct in row
                if i in (0, 1, 2):
                    s = 0
                elif i in (3, 4, 5):
                    s = 3
                else:
                    s = 6
                count1 = s + 3
                
                while s < count1:
                    if j in (0, 1, 2):
                        t = 0
                    elif j in (3, 4, 5):
                        t = 3
                    else:
                        t = 6
                    count2 = t + 3
                    
                    while t < count2:
                        if board[s][t] == value and i != s and j != t:
                            return("\n" + "Not solved, please try again.")
                        t += 1
                    s += 1
                    
        return("\n" + "You've solved it!")


    def sudoku_solver(self, board):
        """
        Given a Sudoku grid, finds the solution and prints out the solved grid.
        """

        if self.recur_solver(board, box=0, cell=0) is True:
            self.print_grid(board)
        else:
            print("There is no solution to this Sudoku puzzle.")


    def recur_solver(self, board, box, cell):
        """
        Recursive helper function for sudoku_solver.
        """

        # have reached the end of the board
        if box == len(board) - 1 and cell == len(board):
            return True
        
        # have reached the end of the 3x3 grid
        if cell == len(board):
            box += 1
            cell = 0
        
        if board[box][cell] == " ":

            # find all values in column
            column = []
            if box in (0, 3, 6):
                s = 0
            elif box in (1, 4, 7):
                s = 1
            else:
                s = 2

            while s < 9:
                if cell in (0, 3, 6):
                    t = 0
                elif cell in (1, 4, 7):
                    t = 1
                else:
                    t = 2

                while t < 9:
                    column.append(board[s][t])
                    t += 3
                s += 3

            # find all values in row
            row = []
            if box in (0, 1, 2):
                s = 0
            elif box in (3, 4, 5):
                s = 3
            else:
                s = 6
            count1 = s + 3
            
            while s < count1:
                if cell in (0, 1, 2):
                    t = 0
                elif cell in (3, 4, 5):
                    t = 3
                else:
                    t = 6
                count2 = t + 3
                
                while t < count2:
                    row.append(board[s][t])
                    t += 1
                s += 1

            # determine what value should be placed in cell
            for i in range(1, 10):
                if (i not in board[box]) and (i not in column) and (i not in row): 
                    board[box][cell] = i

                    # move on to next cell
                    if self.recur_solver(board, box, cell+1) is True:
                        return True
                    else: # there was no valid solution with the value originally placed, place next value
                        board[box][cell] = " "
        else:
            # move on to next cell
            return self.recur_solver(board, box, cell+1)
        
        return False # there was no valid solution


def translate_board(user_input):
    """
    Takes user's input of Sudoku grid and translates it to the format we need.
    """

    user_list = user_input.split() # create array with each number as an element
    board = [] # to hold Sudoku grid

    count = 1
    sub_array = [] # to hold each 3x3 grid
    for i in range(len(user_list)):
        value = int(user_list[i])

        if value == 0: # empty cell
            sub_array.append(" ")
        else:
            sub_array.append(value)
        
        if count == 9: # sub_array holds complete 3x3 grid
            board.append(sub_array)
            sub_array = []
            count = 1
        else:
            count += 1
    
    return board


if __name__ == "__main__":
    path = (input("Would you like to solve a Sudoku puzzle (S), verify your puzzle's solution (V), or generate the solution to your Sudoku puzzle (G)? Please enter the corresponding letter (please input capital letters only): "))
    
    if path == "S": # solve a Sudoku puzzle
        p = SudokuPuzzle()

    elif path == "V": # verify if a completed Sudoku grid was solved correctly
        user_input = input("\n" + "Please input your Sudoku puzzle to verify your solution. Enter the values in your completed grid with each number separated by a space. Every 9 numbers indicates a 3x3 grid. You should enter 81 numbers total (please see README for more details): ")
        grid = translate_board(user_input)
        p = SudokuPuzzle(grid)

    elif path == "G": # generate a solution to a Sudoku grid
        user_input = input("\n" + "Please input your Sudoku puzzle to generate a solution for. Use the number 0 to indicate a blank cell and separate numbers with a space. Every 9 numbers indicates a 3x3 grid. You should enter 81 numbers total (please see README for more details): ")
        
        grid = translate_board(user_input)
        p = SudokuPuzzle(grid)