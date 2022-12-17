'''
game.py - Game board class and methods for TicTacToe

based on:
  https://www.freecodecamp.org/news/python-projects-for-beginners/#tic-tac-toe-python-project

Skills:
- list comprehensions
- classes
- static methods

Added features:
- kwargs (allows check_winner to be called without square/letter)
- getter/setter
- commandline arguments
  
'''
from player import RandomComputerPlayer, HumanPlayer, Player


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self._winner = None
    
    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self,letter):
        self._winner = letter

    def print_board(self):
        """Print the current board
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        """Print the board numbers
        """
        # 1 | 2 | 3 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self) -> list:
        """available_moves

        Returns:
            list: List of available, valid moves (empty squares)
        """
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # ^^^^ list comprehension equivalent of below code
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     # ex: ['x','x','o'] => [(0,x),(1,x),(2,o)]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    
    def empty_squares(self) -> bool:
        """Are there any empty squares

        Returns:
            bool: True if there are empty squares. False if not.
        """
        return ' ' in self.board
    
    def num_empty_squares(self) -> int:
        """Number of empty squares

        Returns:
            int: the number of empty squares
        """
        return len(self.available_moves())
    
    def mark_square(self,square:int,letter:str) -> bool:
        """Mark a square with a letter

        Args:
            square (int): square chosen
            letter (str): player letter

        Returns:
            bool: Whether the move was valid
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            move = { "square":square, "letter":letter}
            self.check_winner(**move)
            return True
        
        return False

    def check_winner(self,**kwargs):
        """Check for a winner from the last move

        Args:
            sq (int): Most recent move
            lt (str): Letter that made the move
        """
        if 'square' in kwargs.keys() and 'letter' in kwargs.keys():
            # Check the row of the move
            row_index = kwargs["square"] // 3 # Divide the square by 3, rounding down
            row = self.board[(row_index * 3) : (row_index + 1) * 3] # Slice the board based on the row_index
            if all(spot == kwargs["letter"] for spot in row):
                self.winner = kwargs["letter"]
                return
            
            # Check the col of the move
            col_index = kwargs["square"] % 3 # Get the mod3 result for the column
            col = [self.board[col_index+i*3] for i in range(3)] # list comprehension to do: col_index+0, col_index+3, col_index+6
            if all(spot == kwargs["letter"] for spot in col):
                self.winner = kwargs["letter"]
                return

            # Check the diagonals if the move is on one
            if kwargs["square"] % 2 == 0:
                diagonal1 = [self.board[i] for i in [0,4,8]]
                if kwargs["square"] in [0,4,8]:
                    if all(spot == kwargs["letter"] for spot in diagonal1):
                        self.winner = kwargs["letter"]
                        return

                diagonal2 = [self.board[i] for i in [2,4,6]]
                if kwargs["square"] in [2,4,6]:
                    if all(spot == kwargs["letter"] for spot in diagonal2):
                        self.winner = kwargs["letter"]
                        return

        else:
            for row in [0,1,2]:
                if self.board[row*3] == self.board[(row*3)+1] == self.board[(row*3)+2] != ' ':
                    self.winner = self.board[row*3]
                    return

            for col in [0,1,2]:
                if self.board[col] == self.board[col+3] == self.board[col+6] != ' ':
                    self.winner = self.board[col]
                    return

            if self.board[0] == self.board[4] == self.board[8] != ' ' or self.board[2] == self.board[4] == self.board[6] != ' ':
                self.winner = self.board[4]
                return


def play(game, x_player:Player, o_player:Player, print_game=True):
    letter = 'X'
    # iterate while there are still empty squares and no winner
    while game.empty_squares():
        if print_game:
            game.print_board_nums()

        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        game.mark_square(square,letter)
    
        if print_game:
            print(f'{letter} makes a move to square {square}')
            game.print_board()
            print('')

        if game.winner is not None:
            print(game.winner + ' wins!!')
            return game.winner

        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'
    else:
        print('Tie game! So predictable...')
        return None

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="A password generator implemented in Python.")
    parser.add_argument("-x",action="store_true",help="Set X to be a human player",default=False)
    parser.add_argument("-o",action="store_true",help="Set O to be a human player",default=False)
    args = parser.parse_args()

    x_player = RandomComputerPlayer('x')
    if args.x:
        x_player = HumanPlayer('x')

    o_player = RandomComputerPlayer('o')
    if args.o:
        o_player = HumanPlayer('o')

    game = TicTacToe()
    play(game,x_player,o_player,print_game=True)