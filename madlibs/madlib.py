"""Madlibs
An exercise in string replacement and user input.

This picks a random madlib from the defined set in random_madlibs and cycles through the needed inputs.

"""
import random
import random_madlibs

ml_name = random.choice(list(random_madlibs.madlibs.keys()))
madlib = random_madlibs.madlibs[ ml_name ]
for key in madlib['vars']:
    madlib['text'] = madlib['text'].replace(f'---{key}---',input(madlib['vars'][key]))

print( "\n{}\n{}\n".format( ml_name, madlib['text'] ) )
