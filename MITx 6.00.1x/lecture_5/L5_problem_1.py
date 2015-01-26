def interPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    x = float(base)
    y = float(exp)
    total = x
    
    while y > 1:
        y -= 1
        
        if x ==1:
            total += x
            
        else:
            total *= x

    return round(total, 4)

print interPower(7.78, 7)
        
        
    

