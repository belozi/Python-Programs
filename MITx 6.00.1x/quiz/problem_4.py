def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    how_close = 0.01
    low = 0
    high = x
    guess = high / 2.0
    if guess > 100:
        guess = 20
    while abs((b ** guess) - x) > how_close:
        guess = (low + high) / 2
        if b**guess > x:
            high = guess
        else:
            low = guess
    return guess

print myLog(16, 4)
print myLog(8, 2)
print myLog(1, 1)
print myLog(1000, 2)
