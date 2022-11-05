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
    

'''

import argparse
import random
import string

def complex_enough(password:str,alphabet:str,min_per_class:int) -> bool:
    """Checks to see if there are enough characters in the password from each class in the alphabet

    Args:
        password (str): potential password
        alphabet (str): alphabet of characters
        min_per_class (int): minimum number of characters per class

    Returns:
        bool: Is complex enough?
    """
    class_dict = {
        'alpha' : -1,
        'digit' : -1,
        'punct' : -1
    }
    for char in alphabet:
        if char in string.ascii_lowercase + string.ascii_uppercase:
            class_dict['alpha'] = 0
        if char in string.digits:
            class_dict['digit'] = 0
        if char in string.punctuation:
            class_dict['punct'] = 0

    for char in password:
        if char in string.ascii_lowercase + string.ascii_uppercase:
            class_dict['alpha'] += 1
        if char in string.digits:
            class_dict['digit'] += 1
        if char in string.punctuation:
            class_dict['punct'] += 1

    for char_class in class_dict.keys():
        if class_dict[char_class] > -1 and class_dict[char_class] < min_per_class:
            return False
    
    return True

def generate_password(alphabet:string,config:dict) -> str:
    """Generates a password

    Args:
        alphabet (string): alphabet of characters to use
        length (int): length of the password to generate
        min_per_class (int): minimum number of characters per character class

    Returns:
        str: password
    """
    if (config.minchar * config.complexity) > config.length:
        raise argparse.ArgumentError(argument=None,message='Length ({}) does not support complexity ({}) and minimum character ({}) requirements. Try a longer length.'.format(config.length,config.complexity,config.minchar))

    password = ''
    while len(password) < config.length:
        password += random.choice(alphabet)

    if complex_enough(password,alphabet,config.minchar):
        return password
    
    return(generate_password(alphabet,config))


def get_alphabet(complexity:int) -> str:
    """Get alphabet of characters to create passwords from

    Args:
        complexity (int): complexity class of the password.
                          1 -> letters only
                          2 -> letters + numbers
                          3 -> letters + numbers + punctuation

    Raises:
        argparse.ArgumentError: If we somehow get a complexity class other than 1, 2, or 3

    Returns:
        str: string representation of the alphabet
    """
    if complexity == 1:
        return( string.ascii_lowercase+string.ascii_uppercase )

    if complexity == 2:
        return( string.ascii_lowercase+string.ascii_uppercase+string.digits )

    if complexity == 3:
        return( string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation )
    
    raise argparse.ArgumentError(argument=None,message=f"Unknown complexity: {complexity}")

def remove_excluded(alphabet:str,excluded='') -> str:
    """Removes excluded characters from an alphabet

    Args:
        alphabet (str): alphabet to remove characters from
        exluded (str, optional): characters to remove. Defaults to ''.

    Returns:
        str: new alphabet
    """
    if excluded is not None:
        for char in excluded:
            alphabet = alphabet.replace(char,"")

    return( alphabet )


parser = argparse.ArgumentParser(description="A password generator implemented in Python.")
parser.add_argument("--count","-c",action="store",type=int,help="Number of passwords to generate")
parser.add_argument("--length","-l",action="store",type=int,help="Password length (per password)")
parser.add_argument("--complexity","-x",action="store",type=int,choices=[1,2,3],help="Password complexity. 1 => letters only. 2 => numbers and letters. 3=> numbers, letters, and special characters.", default=3)
parser.add_argument("--exclude","-d",action="store",help="Characters to exclude. Escape special characters if necessary.")
parser.add_argument("--minchar","-m",action="store",type=int,help="Minimum characters per class",default=1)
args = parser.parse_args()

print("Welcome to this Python Password Generator")
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
