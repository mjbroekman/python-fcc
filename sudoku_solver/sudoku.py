'''Solve Sudoku puzzles

Author: Maarten Broekman

Inspired by:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#sudoku-solver-python-project

Skills:
    - list comprehension
    - recursion
    - list membership

Add-ons
    - command-line arguments (argparse)
    - output formatting
    - class / method refactoring instead of functional
    - parse string into puzzle
'''
import argparse

class Board:
    def __init__(self,board:str,delimiter:str = ",",verbose:bool = False):
        self._verbose = verbose
        self._board = [
            [-1,-1,-1, -1,-1,-1, -1,-1,-1],
            [-1,-1,-1, -1,-1,-1, -1,-1,-1],
            [-1,-1,-1, -1,-1,-1, -1,-1,-1],

            [-1,-1,-1, -1,-1,-1, -1,-1,-1],
            [-1,-1,-1, -1,-1,-1, -1,-1,-1],
            [-1,-1,-1, -1,-1,-1, -1,-1,-1],

            [-1,-1,-1, -1,-1,-1, -1,-1,-1],
            [-1,-1,-1, -1,-1,-1, -1,-1,-1],
            [-1,-1,-1, -1,-1,-1, -1,-1,-1],
        ]
        puzzle = board.split(delimiter) # 0, 1, 2, 3, ... 80

        while len(puzzle) < 81:
            puzzle.append('')

        for space in range(81): # 0, 1, 2, 3, ... 80
            row = space // 9
            col = space % 9
            try:
                if puzzle[space] == '':
                    self._board[row][col] = -1
                else:
                    self._board[row][col] = int(puzzle[space])
            except IndexError:
                self._board[row][col] = -1

    def __repr__(self):
        return "%s(%r)" % self.__class__,self._board

    def __str__(self):
        mystring = '    0  1  2    3  4  5    6  7  8\n'
        mystring += '  ---------- ---------- ----------\n'
        for row in range(9):
            mystring += f'{row}|'
            for col in range(9):
                mystring += ' {: }'.format(self._board[row][col])
                if col in [2,5]:
                    mystring += ' |'
                if col == 8:
                    mystring += ' |\n'
            if row in [2,5,8]:
                mystring += '  ---------- ---------- ----------\n'

        return mystring

    def next_empty(self) -> tuple:
        """find the next empty space

        Args:
            puzzle_state (list): current state of the puzzle

        Returns:
            tuple: row, column of the empty space. returns (None,None) if there are no empty spaces
        """
        for row in range(9):
            if -1 in self._board[row]:
                return row, self._board[row].index(-1)
        
        return None,None
    
    def print_title(self,title:str):
        """print a title above the board

        Args:
            title (str): title to print
        """
        if len(title) > 34:
            new_title = title[:34]
            title = new_title

        print('{:^34}'.format(title))
        print('{:^34}'.format("-"*len(title)))
        
    def is_valid(self, guess: int, row: int, col: int) -> bool:
        """Check if the guess is valid for the current board

        Args:
            guess (int): Number to guess
            row (int): Row to put the guess on
            col (int): Column to put the guess on

        Returns:
            bool: does it go there?
        """
        # If the guess is already in the row, return False
        # Alternative method:
        #   row_vals = puzzle_state[row]
        #   if guess in row_vals:
        if guess in self._board[row]:
            return False
        
        # Check the column in each row. If it matches, return False
        # Alternative method 1:
        # col_vals = []
        # for i in range(9):
        #   col_vals.append(puzzle_state[i][col])
        #
        # Alternative method 2 (list comprehension):
        # cols_vals = [puzzle_state[i][col] for i in range(9)]
        #
        # if guess in col_vals
        for col_row in range(9):
            if guess == self._board[col_row][col]:
                return False
        
        # Check the "box". If the guess is already present, return False
        # Alternative method:
        # row_start / col_start : (row // 3) * 3 or (col // 3) * 3
        # for loop from row_start to row_start + 3
        row_box = row // 3 # 0, 1, or 2 depending on which set of 3 rows we're in
        col_box = col // 3 # 0, 1, or 2 depending on which set of 3 cols we're in
        for box_row in range((3 * row_box), (3 * row_box) + 3): # range(0,3) for rows 0,1,2... range(3,6) for 3,4,5... etc
            for box_col in range((3 * col_box), (3 * col_box) + 3):
                if guess == self._board[box_row][box_col]:
                    return False

        return True

    def mark_guess(self, guess: int, row: int, col: int) -> bool:
        if self.is_valid(guess,row,col):
            self._board[row][col] = guess
            if self._verbose:
                self.print_title(f'Current Guess: {guess} @ {row},{col}')
                print(self)
            return True
        return False

    def unmark_space(self,row:int,col:int) -> None:
        self._board[row][col] = -1

def solve_sudoku(board: Board) -> bool:
    """
    Solve the puzzle

    Args:
      board (Board): A Sudoku board object

    Returns:
      bool: Does a solution exist
    """

    # step 1: see where I can go in the puzzle
    row, col = board.next_empty()
    
    # step 1.1: if there were no spaces left, then we're done because we only allow valid guesses
    if row is None:
        return True
    
    # step 2: if there is a space to put a number, see what the valid guesses are and try one.
    for guess in range(1,10): # range(1,10) gives 1, 2, 3, ... 9 (range(a,b) includes a but not b)
        # step 3 & 4 are in the class now
        if board.mark_guess(guess,row,col):
            if solve_sudoku(board):
                return True

        # step 5: reset space to -1 if it's not valid
        board.unmark_space(row,col)        

    # step 6: if nothing works, return False
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A brute-force Sudoku puzzle solver.")
    parser.add_argument("--board","-b",action="store",help="A string-representation of the starting sudoku board.",default="")
    parser.add_argument("--delimit","-d",action="store",default=",",help="The delimiter to split the board on")
    parser.add_argument("--verbose","-v",default=False,action="store_true",help="Be verbose about the solving process. Print out each guess and state")
    args = parser.parse_args()

    if args.board == "":
        board = "3,9,,,5,,,,,,,,2,,,,,5,,,,7,1,9,,8,,,5,,,6,8,,,,2,,6,,,3,,,,,,,,,,,,4,5,,,,,,,,,6,7,,,,5,,4,,1,,9,,,,2,,"
    else:
        board = args.board
    
    puzzle = Board(board,args.delimit,args.verbose)
    puzzle.print_title("STARTING BOARD")
    print(puzzle)
    
    if solve_sudoku(puzzle):
        puzzle.print_title("SOLUTION FOUND")
        print(puzzle)
    else:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('This board is UNSOLVABLE!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!')
