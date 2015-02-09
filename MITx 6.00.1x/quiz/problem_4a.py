def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    guess = 0.0
    result = 0.0

    while b**guess != x:
        if abs(b**guess) > x:
            guess -= 1
            break
        else:
            guess += 1
    return int(guess + .05)
    
    

print myLog(16, 2)
print myLog(15, 3)
print myLog(1000, 2)
print myLog(2, 2)
