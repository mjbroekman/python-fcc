'''
Rock, Paper, Scissors
-----
A classic game of rock, paper, scissors... with an optional twist

Author: Maarten Broekman

Inspired by:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#rock-paper-scissors-python-project

Skills:
    - user input
    - random selection from list
    - f-strings

Add-ons (beyond what the FCC projects showed)
    - Added rules for playing Rock, Paper, Scissors, Lizard, Spock from The Big Bang Theory:
        https://bigbangtheory.fandom.com/wiki/Rock,_Paper,_Scissors,_Lizard,_Spock

usage: rps.py [-h] [-l]

A classic game of rock, paper, scissors... with an optional twist

optional arguments:
  -h, --help     Show this help message and exit
  --rpsls, -l    Play Rock, Paper, Scissors, Lizard, Spock instead.
'''
import argparse
import sys
import random


def play(choices):
    my_choice = random.choice(list(choices.keys()))
    print('I have made my choice...')
    user_choice = ''
    while True:
        while user_choice not in choices.keys():
            user_choice = input('Make your choice:\n\t{}\nWhat shall it be? '.format('\n\t'.join(choices.keys()))).lower().capitalize()
        
        if my_choice != user_choice:
            if my_choice in choices[user_choice].keys():
                verb = choices[user_choice][my_choice]
                return(f'Good play!\n{user_choice} {verb} {my_choice}\nYou win.')

            if user_choice in choices[my_choice].keys():
                verb = choices[my_choice][user_choice]
                return(f'Bad luck!\n{my_choice} {verb} {user_choice}.\nYou lose.')

        print('Stalemate! Pick again!\n\n')
        my_choice = random.choice(list(choices.keys()))
        user_choice = ''


parser = argparse.ArgumentParser(description="An implementation of Rock-Paper-Scissors.")
parser.add_argument("--rpsls","-l",action="store_true",help="Play Rock, Paper, Scissors, Lizard, Spock instead.")
args = parser.parse_args()

choices = {}
if args.rpsls:
    choices = {
        "Rock": {
            'Scissors':'crushes',
            'Lizard':'crushes',
        },
        "Paper": {
            'Rock':'covers',
            'Spock':'disproves',
        },
        "Scissors": {
            'Paper':'cuts',
            'Lizard':'decapitates',
        },
        "Lizard": {
            'Spock':'poisons',
            'paper':'eats',
        },
        "Spock": {
            'Scissors':'smashes',
            'Rock':'vaporizes',
        },
    }
else:
    choices = {
        "Rock": {'Scissors':'crushes'},
        "Paper": {'Rock':'covers'},
        "Scissors": {'Paper':'cuts'},
    }

print('Welcome to {}'.format(', '.join(choices.keys())))
print(play(choices))

