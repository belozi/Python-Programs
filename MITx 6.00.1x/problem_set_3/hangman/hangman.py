lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    pool = "abcdefghijklmnopqrstuvwxyz"

    for l in lettersGuessed:
        if l in pool:
            pool = pool.replace(l, '')

    return pool

print getAvailableLetters(lettersGuessed)

