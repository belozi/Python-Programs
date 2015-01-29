def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    data = []
    for l in secretWord:
        if l in lettersGuessed:
            data.append(l)
        else:
            data.append('_')
    view = " ".join(data)
    return view
    

print getGuessedWord('beet', ['b', 'a', 't'])
