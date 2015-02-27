def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    coder = {}
    new_order = upper[26 - shift :] + upper[: 26 - shift]
    lower = new_order.lower()
    for number in xrange(26):
        n = number+1
        char = 0
        coder[n] = [new_order[char]]
        for key in coder:
            coder[key] = [new_order[char], lower[char]]
            char += 1
    return coder

print buildCoder(3)

        
