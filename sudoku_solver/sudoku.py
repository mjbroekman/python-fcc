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
'''
def find_next_empty(puzzle_state: list) -> tuple:
    """find the next empty space

    Args:
        puzzle_state (list): current state of the puzzle

    Returns:
        tuple: row, column of the empty space. returns (None,None) if there are no empty spaces
    """
    for row in range(9):
        if -1 in puzzle_state[row]:
            return row, puzzle_state[row].index(-1)
    
    return None,None

def is_valid(puzzle_state: list, guess: int, row: int, col: int) -> bool:
    """Check if the guess is valid for the current board

    Args:
        puzzle_state (list): current board
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
    if guess in puzzle_state[row]:
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
        if guess == puzzle_state[col_row][col]:
            return False
    
    # Check the "box". If the guess is already present, return False
    # Alternative method:
    # row_start / col_start : (row // 3) * 3 or (col // 3) * 3
    # for loop from row_start to row_start + 3
    row_box = row // 3 # 0, 1, or 2 depending on which set of 3 rows we're in
    col_box = col // 3 # 0, 1, or 2 depending on which set of 3 cols we're in
    for box_row in range((3 * row_box), (3 * row_box) + 3): # range(0,3) for rows 0,1,2... range(3,6) for 3,4,5... etc
        for box_col in range((3 * col_box), (3 * col_box) + 3):
            if guess == puzzle_state[box_row][box_col]:
                return False

    return True

def solve_sudoku(puzzle_state: list) -> bool:
    """
    Solve the puzzle

    Args:
      puzzle_state (list): list of lists representing the state of the board 
    [
        [ 3,  9, -1,   -1,  5, -1,   -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,   -1, -1,  5],
        [-1, -1, -1,    7,  1,  9,   -1,  8, -1],

        [ 3,  9, -1,   -1,  5, -1,   -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,   -1, -1,  5],
        [-1, -1, -1,    7,  1,  9,   -1,  8, -1],

        [ 3,  9, -1,   -1,  5, -1,   -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,   -1, -1,  5],
        [-1, -1, -1,    7,  1,  9,   -1,  8, -1],
    ]

    Returns:
      bool: Does a solution exist
    """

    # step 1: see where I can go in the puzzle
    row, col = find_next_empty( puzzle_state )
    
    # step 1.1: if there were no spaces left, then we're done because we only allow valid guesses
    if row is None:
        return True
    
    # step 2: if there is a space to put a number, see what the valid guesses are and try one.
    for guess in range(1,10): # range(1,10) gives 1, 2, 3, ... 9 (range(a,b) includes a but not b)
        # step 3: check if this is valid
        if is_valid(puzzle_state,guess,row,col):
            puzzle_state[row][col] = guess 
            # step 4: recursively solve
            if solve_sudoku(puzzle_state):
                return True
        
        # step 5: reset space to -1 if it's not valid
        puzzle_state[row][col] = -1

    # step 6: if nothing works, return False
    return False

if __name__ == '__main__':
    example_board = [
        [ 3,  9, -1,   -1,  5, -1,   -1, -1, -1],
        [-1, -1, -1,    2, -1, -1,   -1, -1,  5],
        [-1, -1, -1,    7,  1,  9,   -1,  8, -1],

        [-1,  5, -1,   -1,  6,  8,   -1, -1, -1],
        [ 2, -1,  6,   -1, -1,  3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1,  4],
        
        [ 5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [ 6,  7, -1,    1, -1,  5,   -1,  4, -1],
        [ 1, -1,  9,   -1, -1, -1,    2, -1, -1]
    ]
    if solve_sudoku(example_board):
        print('       SOLUTION FOUND')
        print('       ==============')
        print('   0 1 2   3 4 5   6 7 8')
        print('  ------- ------- -------')
        for row in range(9):
            print(f'{row}|',end="")
            for col in range(9):
                print('{: }'.format(example_board[row][col]),end="")
                if col in [2,5]:
                    print(' |',end="")
                if col == 8:
                    print(' |')
            if row in [2,5,8]:
                print('  ------- ------- -------')
