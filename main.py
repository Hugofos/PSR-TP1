import sys
import random

from functions import *

def playGame(utm, mv):
    words = getWords()
    for i in range(0, 2):
        word = random.choice(words)
        print(word)
        t = input('Write word: ')
        print('You typed: ' + t)
        verifyWord(t, word)

def main():
    args = sys.argv[1:]
    mv = 0
    print(args)
    print('-utm' in args or '--use_time_mode' in args)
    print('-mv' in args or '--max_value' in args)
    print('-uw' in args or '--use_words' in args)

    utm = ('-utm' in args or '--use_time_mode' in args)

    if '-mv' in args:
        mv = args.index('-mv')
        playGame(utm, mv)

    if '--max_value' in args:
        mv = args.index('--max_value')
        playGame(utm, mv)

    if '-h' in args or '--help' in args:
        printHelpMessage()

if __name__ == '__main__':
    main()
