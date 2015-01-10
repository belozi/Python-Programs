import random
HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
===========''', '''
    +---+
    |   |
    0   |
        |
        |
        |
===========''', '''
    +---+
    |   |
    0   |
    |   |
        |
        |
===========''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
===========''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
===========''','''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
===========''','''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
===========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # THis function returns a random string from the list of passed strings.
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missed letters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end= ' ')
    print()

    blanks = '_' * len(secretWord)):
