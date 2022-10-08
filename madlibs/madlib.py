"""Madlibs
An exercise in string replacement and user input.

This picks a random madlib from the defined set in random_madlibs and cycles through the needed inputs.

"""
import random
import random_madlibs

madlib = random_madlibs.madlibs[random.choice(list(random_madlibs.madlibs.keys()))]
for key in madlib['vars']:
    madlib['text'] = madlib['text'].replace(f'---{key}---',input(madlib['vars'][key]))

print()
print(list(random_madlibs.madlibs.keys()))
print(madlib['text'])