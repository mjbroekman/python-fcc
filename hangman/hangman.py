'''
Hangman
-------
The Classic Game of Hangman

Author: Maarten Broekman

Inspired by:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#hangman-python-project

Skills:
    - user input
    - random selection from list
    - f-strings
    - string replacement
    - list comparison
    - list membership

Add-ons (beyond what the FCC projects showed)
    - reading from files
    - reading from Internet source
    - alternate game display

usage: hangman.py [-h] [-f file] [-u url]

A classic game of hangman...

optional arguments:
  -h, --help             Show this help message and exit
  --file FILE, -f FILE   Use FILE as the word source
  --url, -u              Treat FILE as a URL instead of a local file
  --wof, -w              Use Wheel of Fortune rules and pre-reveal the letters rstlne
'''

import argparse
import json
import mimetypes
from operator import indexOf
import os
import random
import re
import requests
import string
import sys


def get_word(file: str,url: bool) -> str:
    if os.path.exists(file) and not url:
        mime_type = mimetypes.guess_type(file)
        with open(file) as word_list:
            words = word_list.read()
            if mime_type[0] is None or mime_type[0] == "text/plain":
                words = words.split('\n')
                words = [i for i in words if i] # Remove empty strings in case there were blank lines
                return random.choice(words)
        
            if mime_type[0] == "application/json":
                words = json.loads(words)
                if 'data' in words.keys():
                    return random.choice(words['data'])
                if 'words' in words.keys():
                    return random.choice(words['words'])
                if 'word_list' in words.keys():
                    return random.choice(words['word_list'])
                
    if url and "http" in file and "://" in file:
        response = requests.get(file)
        if response.headers['Content-Type'] == "application/json":
            resp_text = json.loads(response.text)
            if 'data' in resp_text.keys():
                return random.choice(resp_text['data'])
            if 'words' in resp_text.keys():
                return random.choice(resp_text['words'])
            if 'word_list' in resp_text.keys():
                return random.choice(resp_text['word_list'])

    print(f'Unable to load words from {file}. I can read plain ASCII and JSON from local files or from URLs')
    print("For plain ASCII files, make sure each word is on it's own line")
    print("For JSON files, make sure there is _one_ of the following elements:\n\t- data\n\t- words\n\t- word_list")
    print("See words.json for an example.")
    sys.exit(1)

def reveal(word: str, hidden: list) -> str:
    for letter in hidden:
        word = re.sub(letter,"_",word)
    
    return word

def hangman(state: int):
    """Display the hangman and scaffold

    Args:
        state (int): how much of the scaffold and hangman is revealed
    
    /==========\
     ||        |
     ||        =
     ||        \O
     ||        /|\
     ||         |
     ||        / \
     ||
    /||\
    """
    if state == 1:
        print("""
            /=======\\
            ||
            ||
            ||
            ||
            ||
            ||
            ||
           /||\\
        """)
    
    if state == 2:
        print("""
            /=======\\
            ||      |
            ||      =
            ||      \\
            ||
            ||
            ||
            ||
           /||\\
        """)
    
    if state == 3:
        print("""
            /=======\\
            ||      |
            ||      =
            ||      \\O
            ||
            ||
            ||
            ||
           /||\\
        """)

    if state == 4:
        print("""
            /=======\\
            ||      |
            ||      =
            ||      \\O
            ||       |
            ||       |
            ||
            ||
           /||\\
        """)

    if state == 5:
        print("""
            /=======\\
            ||      |
            ||      =
            ||      \\O
            ||      /|
            ||       |
            ||
            ||
           /||\\
        """)

    if state == 6:
        print("""
            /=======\\
            ||      |
            ||      =
            ||      \\O
            ||      /|\\
            ||       |
            ||
            ||
           /||\\
        """)

    if state == 7:
        print("""
            /=======\\
            ||      |
            ||      =
            ||      \\O
            ||      /|\\
            ||       |
            ||      /
            ||
           /||\\
        """)

    if state == 8:
        print("""
            /=======\\
            ||      |
            ||      =
            ||      \\O
            ||      /|\\
            ||       |
            ||      / \\
            ||
           /||\\
        """)


def play(word: string,hang: bool,wof_rules: bool):
    hangman_state = 0
    print("You can make {} incorrect guesses ...".format(8 - hangman_state))
    hidden = list(string.ascii_lowercase)
    guessed = []
    if wof_rules:
        print("... using Wheel of Fortune rules. Revealing r, s, t, l, n, e")
        for letter in ['r','s','t','l','n','e']:
            hidden.remove(letter)
            guessed.append(letter)

    current_state = reveal(word,hidden)
    while hangman_state < 8:
        print(re.sub("_"," _ ",current_state))
        if guessed:
            print("- Already guessed: [ " + ", ".join(guessed) + " ]")
        print("You have {} incorrect guesses remaining. ".format(8 - hangman_state))
        next_guess = input('What is the next letter you wish to reveal? ').lower()
        if next_guess in guessed:
            print(f'{next_guess} has already been guessed...')
            continue

        if next_guess == word:
            print(f"Congratulations! You guessed the word without revealing all the letters!\n")
            sys.exit(0)

        if next_guess not in list(string.ascii_lowercase):
            print(f'{next_guess} is not a valid character. Please only guess the letters a to z.')
            hangman_state = hangman_state + 1
        else:
            guessed.append(next_guess)
            hidden.remove(next_guess)

        new_state = reveal(word,hidden)
        try:
            new_state.index("_") 
        except ValueError:
            print(f"\nCongratulations! You found the word!\n\n\t{new_state}\n\n")
            sys.exit(0)

        if new_state == current_state:
            hangman_state = hangman_state + 1
        
        current_state = new_state
        if hang:
            hangman(hangman_state)

    print("I'm sorry... You lose...")
    print(f'The word was:\n\t{word}\n')
    sys.exit(0)

parser = argparse.ArgumentParser(description="An implementation of Hangman.")
parser.add_argument("--file","-f",action="store",help="Use the specified file as a word source.",default="words.json")
parser.add_argument("--url","-u",action="store_true",help="Treat FILE as a URL instead of a local file.")
parser.add_argument("--wof","-w",action="store_true",help="Use Wheel of Fortune rules and reveal rstlne at the start.")
parser.add_argument("--hang",action="store_true",help="Show the scaffold, noose, and body")
args = parser.parse_args()

try:
    play(get_word(args.file,args.url).lower(),args.hang,args.wof)
except KeyboardInterrupt as ke:
    print("Exiting...")
