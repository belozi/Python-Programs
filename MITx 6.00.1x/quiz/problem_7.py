def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    while n >= 6:
        if n % 6== 0:
            n -=6
        elif n % 9 == 0:
            n -=9
        elif n >= 20:
            n -= 20
        elif n >= 9:
            n -= 9
        elif n >= 6:
            n -= 6
    if n == 0:
        return True
    else:
        return False

print McNuggets(6)
print McNuggets(9)
print McNuggets(20)
print McNuggets(236)
print McNuggets(45)
print McNuggets(133)
print McNuggets(239)
print McNuggets(32)
