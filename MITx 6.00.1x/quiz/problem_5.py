def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    longest = None
    string = ''
    if len(s1) >= len(s2):
        longest = s1
    else:
        longest = s2
    for x in range(len(longest)):
        try:
            string += s1[x]
        except:
            pass
        try:
            string += s2[x]
        except:
            pass

    return string

print laceStrings("1357", "2468123")

