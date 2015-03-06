def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    max_words = 0
    best_shift = 0
    shift = 0
    while shift < 26:
        count = 0
        data = applyShift(text, shift)
        words = data.split(' ')
        for word in words:
            if isWord(wordList, word):
                count +=1
        if count > max_words:
            max_words = count
            best_shift = shift
        shift += 1
        
    return best_shift

print findBestShift(wordList, 'TQxxa, iAdxp!')   
