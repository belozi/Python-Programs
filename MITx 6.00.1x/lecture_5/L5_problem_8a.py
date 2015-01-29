def isIn(char, aStr):
    if aStr == "":
        return False
    guess = len(aStr)/2
    if aStr[guess] == "":
        return False
    elif aStr[guess] == char:
        return True
    elif char > aStr[-1] or char < aStr[0]:
        return False
    elif aStr[guess] > char:
        aStr = aStr[:guess]
    else:
        aStr = aStr[guess:]
    return isIn(char, aStr)
        

print isIn("a", "")
                 
