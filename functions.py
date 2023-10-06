import urllib.request

from colorama import Fore, Back, Style

def getWords():
    word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    return words

def printHelpMessage():
    print("""optional arguments:
        -h, --help
                            show this help message and exit

        -utm, --use_time_mode
                            Max number of secs for time mode or maximum number of inputs for number of inputs mode.

        -mv MAX_VALUE, --max_value MAX_VALUE
                            Max number of seconds for time mode or maximum number of inputs for number of inputs mode.

        -uw, --use_words
                            Use word typing mode, instead of single character typing.""")

def verifyWord(typedWord, word):
    for l in range(len(list(typedWord))):
        try:
            if typedWord[l] == word[l]:
                print(Back.GREEN + typedWord[l] + Style.RESET_ALL)
            else:
                print(Back.RED + typedWord[l] + Style.RESET_ALL)
        except:
            print(Back.RED + typedWord[l] + Style.RESET_ALL)