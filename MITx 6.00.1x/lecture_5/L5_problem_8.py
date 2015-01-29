def IsIn(char, aStr):
    low = 0
    high = len(aStr)
    guess = -1
    guesses = high - 1

    if aStr == "":
        return False
    while guesses > 0 and aStr[guess] != char:
        guess = (low + high) / 2
        if aStr[guess] > char:
            high = guess
            print "high: " + str(guess)
        else:
            low = guess
            print "low: " + str(guess)
        guesses -= 1
    if aStr[guess] == char:
        return True
    else:
        return False
    

print IsIn("b", "")
                 
