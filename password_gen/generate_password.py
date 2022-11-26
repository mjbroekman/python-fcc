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
'''

import argparse
import random
import string

class PasswordConfig:
    """PasswordConfig object

    """
    def __init__(self,alphabet:str,minchar:int,complexity:int,length:int):
        self.alphabet = alphabet
        self.minchar = minchar
        self.complexity = complexity
        self.length = length


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

def generate_password(config:PasswordConfig) -> str:
    """Generates a password

    Args:
        alphabet (string): alphabet of characters to use
        config (dict): configuration dict structure
                       must include:
                         'length' (int)     : length of desired password
                         'minchar' (int)    : minimum characters per class
                         'complexity' (int) : complexity of password

    Returns:
        str: password
    """
    if (config.minchar * config.complexity) > config.length:
        raise argparse.ArgumentError(argument=None,message='Length ({}) does not support complexity ({}) and minimum character ({}) requirements. Try a longer length.'.format(config.length,config.complexity,config.minchar))

    password = ''
    while len(password) < config.length:
        password += random.choice(config.alphabet)

    if complex_enough(password,config.alphabet,config.minchar):
        return password
    
    return(generate_password(config))


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
