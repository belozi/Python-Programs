def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    coder = {}
    old_order = upper + lower
    new_upper =  upper[ shift : ] + upper[ : shift + 1]
    new_lower = lower[ shift : ] + lower[ : shift + 1]
    
    for x in xrange(26):
        coder[old_order[x]] =new_upper[x]
    for x in xrange(26,52):
        coder[old_order[x]] =new_lower[x - 26]
    return coder, old_order

print buildCoder(3)

        
