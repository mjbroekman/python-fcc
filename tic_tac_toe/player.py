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
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter:str):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            try:
                val = int(input(self.letter + "\'s turn. Input move [0-8]: "))
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again!')
        
        return val

