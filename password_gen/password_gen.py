'''
Python Password Generator

Inspired by:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#password-generator-python-project

Skills:
    - user input
    - looping constructs

Add-ons:
    - command-line arguments
        - limited choices for argument values
    - complexity checking
    - raising exceptions
    - docstrings
    - import modules

'''

import argparse
from generate_password import remove_excluded, get_alphabet, generate_password

parser = argparse.ArgumentParser(description="A password generator implemented in Python.")
parser.add_argument("--count","-c",action="store",type=int,help="Number of passwords to generate")
parser.add_argument("--length","-l",action="store",type=int,help="Password length (per password)")
parser.add_argument("--complexity","-x",action="store",type=int,choices=[1,2,3],help="Password complexity. 1 => letters only. 2 => numbers and letters. 3=> numbers, letters, and special characters.", default=3)
parser.add_argument("--exclude","-d",action="store",help="Characters to exclude. Escape special characters if necessary.")
parser.add_argument("--minchar","-m",action="store",type=int,help="Minimum characters per class",default=1)
args = parser.parse_args()

print("Welcome to this Password Generator implemented in Python...")
if not args.count:
    args.count = -1
    while args.count < 1:
        args.count = int(input("How many passwords should be generated? "))

if not args.length:
    args.length = -1
    while args.length < 2:
        args.length = int(input("Password length: "))

print("... generating " + str(args.count) + " passwords",end="")
print(" of at least " + str(args.length) + " characters from the following character set:")

alphabet = remove_excluded(get_alphabet(args.complexity,),args.exclude)

print("\t" + alphabet + "\n")
count = 1
while count <= args.count:
    print(f"\t{count}: " + generate_password(alphabet,args))
    count += 1
