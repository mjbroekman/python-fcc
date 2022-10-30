'''
Countdown Timer

Inspired by:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#countdown-timer-python-project

Skills:
    - user input
    - type conversion
    - working with time()

Add-ons:
    - exception handling
    - additional user input
    - 'reasonable' bounds checking
    - command-line arguments

'''
import argparse
import sys
import time

def countdown(duration:int, message:str):
    while duration:
        minutes, seconds = divmod(duration,60)
        clear = "       "

        if minutes > 999:
            print('Oh, come on... be reasonable... Over 1000 minutes is just silly. Try a smaller number.')
            sys.exit(1)

        if minutes < 100:
            timer = '{:02d}:{:02d}'.format(minutes,seconds)
        else:
            timer = '{:03d}:{:02d}'.format(minutes,seconds)

        print(clear,end="\r")
        print(timer,end="\r")

        time.sleep(1)
        duration -= 1
    
    if message:
        print(f'{message}')
    else:
        print('Timer completed!')

parser = argparse.ArgumentParser(description="A Python Countdown Timer.")
parser.add_argument("--duration","-d",action="store",type=int,help="The duration of the countdown timer.",default=0)
parser.add_argument("--message","-m",action="store",type=str,help="Optional message to display.",default="Timer completed!")
args = parser.parse_args()

if args.duration < 1:
    args.duration = input('Enter the countdown time in seconds: ')

try:
    countdown(int(args.duration),args.message)
except KeyboardInterrupt as ke:
    print('Exiting...')
