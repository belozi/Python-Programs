import string

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    chars = []
    
    for letter in text:
        if letter == "," or letter in string.digits:
            chars.append(letter)
        elif letter in string.punctuation or letter ==" ":
            chars.append(letter)     
        else:
            chars.append(coder[letter])

    return ''.join(chars)
       
