def f(x):
    import math
    return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    start = float(start)
    if f(start) == f(stop):
        return 0
    return step * f(start) + radiationExposure(start + step, stop, step)


print radiationExposure(14, 20, 0.1)
