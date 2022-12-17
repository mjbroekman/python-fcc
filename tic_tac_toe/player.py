'''
player.py - The player object for tic-tac-toe

based on:
  https://www.freecodecamp.org/news/python-projects-for-beginners/#tic-tac-toe-python-project

Skills:
- class inheritence
- exceptions

Added features:
- getter/setter


'''
import math
import random

class Player:
    def __init__(self, letter:str):
        """Initialization function

        Args:
            letter (_type_): _description_
        """
        self._letter = letter

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self,letter):
        self._letter = letter.upper()

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter:str):
        super().__init__(letter)
    
    def get_move(self, game, print_game):
        if print_game:
            pass
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter:str):
        super().__init__(letter)
    
    def get_move(self, game, print_game):
        valid_square = False
        val = None
        if print_game:
            game.print_board_nums()

        while not valid_square:
            try:
                val = int(input(self.letter + "\'s turn. Input move [0-8]: "))
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again!')
        
        return val

class StrategicComputerPlayer(Player):
    def __init__(self, letter:str,strategy:str):
        super().__init__(letter)
        self._strategy = strategy
    
    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self,strat):
        self._strategy = strat
    
    def get_move(self, game, print_game):
        if print_game:
            pass

        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
            if self.strategy == "optimal":
                square = random.choice(game.available_moves())
            if self.strategy == "corner":
                square = random.choice([0,2,4,6,8])
            if self.strategy == "side":
                square = random.choice([1,3,4,5,7])

        else:
            # Get best move based on minimax algorithm
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, state, player):
        max_player = self.letter # yourself
        other_player = 'O' if player == 'X' else 'X' # set opposing player to the other player

        # first, check to see if the previous move was a winner
        # base case
        # return position and minimax score so we can keep track of outcomes
        if state.winner == other_player:
            # if the _current_ state has a winner, return no position and the appropriate score
            return {
                    'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }

        elif not state.available_moves():
            # if there is no winner and no available moves, return no position and a score of 0 (tie)
            return { 'position': None, 'score': 0 }

        if player == max_player:
            best = { 'position': None, 'score': -math.inf } # (maximize) any new score for you will be better than this
        else:
            best = { 'position': None, 'score': math.inf } # (minimize) any new score for the opponent will be 'better' than this

        for possible_move in state.available_moves():
            # step 1: make a move, try the spot
            state.mark_square(possible_move,player)
            # step 2: recurse with minimax to simulate the game after making the move
            sim_score = self.minimax(state,other_player)
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.winner = None
            sim_score['position'] = possible_move
            # step 4: update dict if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
            
        return best