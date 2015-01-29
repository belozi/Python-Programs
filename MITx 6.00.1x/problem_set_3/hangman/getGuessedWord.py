def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    def data_create(l, secretWord):
        data = []    
        if l in secretWord:
            data.append(l)
            print data
            secretWord = secretWord.replace(l, '')
            return data_create(l, secretWord)
        else:
            data.append('_')
            print data
            secretWord = secretWord.replace(l, '')
            return data_create(l, secretWord)    
    
    for l in lettersGuessed:
        return data_create(l, secretWord)
    

print getGuessedWord('beet', ['b', 'a', 't'])
