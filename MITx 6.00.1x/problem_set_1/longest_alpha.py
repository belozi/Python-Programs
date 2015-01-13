s = 'azcbobobegghakl'

def current_string(string):
    z = None
    current = []
    longest = []
    for x in s:
        if x > z:
            current.append(x)
            z = x
        else:
            if len(current) > len(longest):
                    longest = current
                    current = []
    return('Longest substring in alphabetical order is: ' + ''.join(longest))

print current_string(s)
