'''
Guess
-----
A guessing game of variable difficulty.

Options:
  --low: the lowest number. Default is 0
  --high: the highest number. Default is 10
  --guesses: number of guesses. Default is 3

'''

import argparse
import sys
import random

from fractions import Fraction

parser = argparse.ArgumentParser(description="A Guessing Game of variable difficulty.")
parser.add_argument("--low","-l",action="store",type=int,help="The lowest number of the range to guess from.",default=0)
parser.add_argument("--high","-H",action="store",type=int,help="The highest number of the range to guess from.",default=10)
parser.add_argument("--guess","-g",action="store",type=int,help="The number of guesses available.",default=3)
args = parser.parse_args()

if args.low > args.high:
    args.low, args.high = args.high, args.low

if args.low == args.high:
    print("That's not much a challenge... be serious")
    sys.exit(2)

width = args.high - args.low
bin_tree = 2 ** args.guess

if Fraction(width,bin_tree) <= 1:
    print("That's not very challenging. Maybe try a wider range of numbers or fewer guesses.")
    sys.exit(2)

target_number = random.randint(args.low,args.high)
user_guess = args.low - 1
guess_num = 1
print(f"Guess a number between {args.low} and {args.high}. You have {args.guess} or fewer guesses to do this.")
while guess_num <= args.guess:
    user_guess = int(input(f"Guess a number ({guess_num}): "))
    if args.low <= user_guess <= args.high:
        if user_guess < target_number:
            print("Good guess, but you're too low. Try again.")
            guess_num += 1
        elif user_guess > target_number:
            print("Good guess, but you're too high. Try again.")
            guess_num += 1
        else:
            print("Amazing! You guessed the number!")
            break
    else:
        print("Come on. At least guess a number in the range...")
else: # No break
    print(f"That was tough. You ran out of guesses. The number I was thinking of was {target_number}.")

