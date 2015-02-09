def fixedPoint(f, epsilon):
    guess = 1.0
    for i in range(100):
        if f(guess) - guess < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess

def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)

print sqrt(25)
