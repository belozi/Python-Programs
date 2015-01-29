def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for l in lettersGuessed:
        if l in secretWord:
            secretWord = secretWord.replace(l, '')
    if secretWord == '':
        return True
    else:
        return False


print isWordGuessed('beet', ['b', 'e', 't'])
