def gcIter(a, b):
    x = a
    while x > 0:
        if (b % x) == 0 and (a % x) == 0:
            return x
        else:
            x -= 1


print gcIter(17, 12)

