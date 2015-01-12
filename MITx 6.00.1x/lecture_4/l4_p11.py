def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    v = ['a', 'e', 'i', 'o', 'u']
    c = char.lower()
    for x in v:
        if x == c:
            return True
            break
    return False
 
       
