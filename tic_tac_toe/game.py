'''
game.py - Game board class and methods for TicTacToe

based on:
  https://www.freecodecamp.org/news/python-projects-for-beginners/#tic-tac-toe-python-project
  
'''
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # ^^^^ list comprehension equivalent of below code
        # moves = []
        # for (i,spot) in enumerate(self.board):
        #     # ex: ['x','x','o'] => [(0,x),(1,x),(2,o)]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    # iterate while there are still empty squares and no winner
    while game.empty_squares():
        pass