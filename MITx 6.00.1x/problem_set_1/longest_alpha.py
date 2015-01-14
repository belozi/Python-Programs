s = 'azcbobobegghakl'
"""
def current_string(string):
    z = None
    current = []
    longest = []
    for char in s:
        if char > z:
            current.append(char)
            z = char
            print('in the if statement, x = ' + z)
        elif len(current) > len(longest):
            longest = current
            current = []
            z = None
            print('in the else statement, current = ' + ''.join(longest))
        else:
            continue
    return('Longest substring in alphabetical order is: ' + ''.join(longest)) 

print current_string(s)

"""

for char in s:
    print char
