'''
Guess
-----
A guessing game of variable difficulty.

Author: Maarten Broekman

Inspired by:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#guess-the-number-game-python-project-computer-
    https://www.freecodecamp.org/news/python-projects-for-beginners/#guess-the-number-game-python-project-user-

Skills:
    - user input
    - random number generation
    - f-strings
    - Fraction usage
    - loop-else clauses

usage: guess.py [-h] [--low LOW] [--high HIGH] [--guess GUESS] [--comp]

A Guessing Game of variable difficulty.

optional arguments:
  -h, --help            show this help message and exit
  --low LOW, -l LOW     The lowest number of the range to guess from.
  --high HIGH, -H HIGH  The highest number of the range to guess from.
  --guess GUESS, -g GUESS
                        The number of guesses available.
  --comp, -c            Make the program guess the number.
'''

import argparse
from operator import contains
import sys
import random

from fractions import Fraction

def user_game(low, high, guess):
    target_number = random.randint(low,high)
    user_guess = low - 1
    guess_num = 1
    print(f"Guess a number between {low} and {high}. You have {guess} or fewer guesses to do this.")
    while guess_num <= guess:
        user_guess = int(input(f"Guess a number ({guess_num}): "))
        if low <= user_guess <= high:
            guess_num += 1
            if user_guess < target_number:
                print("Good guess, but you're too low. Try again.\n")
            elif user_guess > target_number:
                print("Good guess, but you're too high. Try again.\n")
            else:
                print("Amazing! You guessed the number!\n")
                break
        else:
            print("Come on. At least guess a number in the range...")
    else: # No break
        print(f"\nThat was tough. You ran out of guesses. The number I was thinking of was {target_number}.")

def comp_game(low, high, guess):
    print(f"I'm going to guess a number between {low} and {high}. I have {guess} or fewer guesses to get it.")
    guess_num = 1
    valid_feedback = [ 'H', 'L', 'C' ]
    while guess_num <= guess:
        comp_guess = low + int( (high - low) / 2 )
        feedback = ''
        feedback = input(f"I'm going to guess: {comp_guess}. Is that high (H), low (L), or correct (C)? ")
        while feedback.capitalize() not in valid_feedback:
            print("I'm sorry. I didn't understand your feedback.")
            feedback = input(f"I'm going to guess: {comp_guess}. Is that high (H), low (L), or correct (C)? ")

        guess_num += 1
        if feedback.capitalize() == 'H':
            high = comp_guess - 1
            print(f"Hmmm. I was too high with {comp_guess}. Let me try again. This time between {low} and {high}\n")
        if feedback.capitalize() == 'L':
            low = comp_guess + 1
            print(f"Hmmm. I was too low with {comp_guess}. Let me try again. This time between {low} and {high}\n")
        if feedback.capitalize() == 'C':
            print("Amazing! I was able to guess your number! Computers are really smart, aren't we?\n")
            break
    else: # No break
        print("\nWow! That was tough. I ran out of guesses.")

parser = argparse.ArgumentParser(description="A Guessing Game of variable difficulty.")
parser.add_argument("--low","-l",action="store",type=int,help="The lowest number of the range to guess from.",default=0)
parser.add_argument("--high","-H",action="store",type=int,help="The highest number of the range to guess from.",default=10)
parser.add_argument("--guess","-g",action="store",type=int,help="The number of guesses available.",default=3)
parser.add_argument("--comp","-c",action="store_true",help="Make the program guess the number.")
args = parser.parse_args()

# Swap the high and low of the range to avoid silliness
if args.low > args.high:
    args.low, args.high = args.high, args.low

# Bail out if the high and low are the same
if args.low == args.high:
    print("That's not much a challenge... be serious")
    sys.exit(2)

# Calculate the width and optimal guess count 
width = args.high - args.low
bin_tree = 2 ** args.guess

# If a binary tree is GUARANTEED to find the right answer, then it's too easy
if Fraction(width,bin_tree) <= 1:
    print("That's not very challenging. Maybe try a wider range of numbers or fewer guesses.")
    sys.exit(2)

if args.comp:
    comp_game(args.low,args.high,args.guess)
else:
    user_game(args.low,args.high,args.guess)
