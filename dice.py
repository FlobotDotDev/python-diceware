'''
Created by majesticflo
Apr 2021
'''

import random, re, string, argparse

words = []
punc = string.punctuation

# Grabs a random number [1-6] five times
def getNum():
    finalNum = ""

    for num in range(5):
        finalNum += str(random.randrange(1,7))

    return finalNum

# Parses through the dicelist.txt and finds the line with the matching number
def getWord(num):
    file = open("./diceware.txt", "r")

    for line in file:
        if re.search(num, line):
            wordSplit = line.split("\n")
            wordSplit = wordSplit[0].split("\t")

    return wordSplit[1]

def passwd():
    finalPass = ""

    # Gets the argument from the user and calls the getWord func n times
    for i in range(numOfWords):
        words.append(getWord(getNum()))

    # Checks the len of the list of words and rotates between them adding them to the finalPass var at the end
    for w in range(len(words)):
        curWord = words[w]
        getPunc = punc[random.randrange(len(punc))]

        # 50/50 chance of being capitalized
        if random.randrange(2) == 1:
            curWord = curWord.capitalize()

        # If last word then print num instead of punc
        if w == len(words) - 1:
            finalPass += curWord

            # Adds n amount of nums to the end of the passwd
            for n in range(random.randrange(1,5)):
                finalPass += str(random.randrange(1,10))

        # Prints a random punc as the seperator between words
        else:
            finalPass += curWord + getPunc

    return finalPass

# Argument parser
parser = argparse.ArgumentParser(description='''
Random password generator based on simulated dice rolls.
''')

# Argument to specify how many words are going to be in the passwd
parser.add_argument('number', help='n words in password', type=int)
numOfWords = vars(parser.parse_args())["number"]

# Calls the passwd func and adds special chars and upper if user answered yes
print("Password = " + passwd())
