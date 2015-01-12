    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    
def clip(lo, x, hi):
    y = max(lo, x)
    z = min(hi, y)

    return z
