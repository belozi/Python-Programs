def iterPower(base, exp):
    total = 0

    if exp == 0:
        return 1

    while exp >= 0:
            total = total *  base
            if exp > 0:
                total = total * base
                exp -= 1

            return total

print iterPower(3, 4)
        
        
    

'''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''

"""
    x = float(base)
    y = float(exp)
    total = x

    while y >= 0:
        total *= total * x
        y -= 1

    return round(total, 4)

print iterPower(7.78, 7)

"""
