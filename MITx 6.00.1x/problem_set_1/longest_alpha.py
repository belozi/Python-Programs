s = 'qwlddiwatapmdrjmzsa'

def current_string(string):
    z = None
    current = []
    longest = []
    for char in s:
        if char >= z:
            z = char
            current.append(z)
            #print ("if current: " + ''.join(current))
            #print ("if longest: " + ''.join(longest))
            if len(current) > len(longest):
                longest = current
        elif char < z:
            if len(current) > len(longest):
                #longest = current
                current = []
                z = char
                current.append(z)
                #print ("elif current: " + ''.join(current))
                #print ("elif longest: " + ''.join(longest))
            else:
                current = []
                current.append(char)
                z = char
                #print ("else current: " + ''.join(current))
                #print ("else longest: " + ''.join(longest))             
            
                
    return('Longest substring in alphabetical order is: ' + ''.join(longest)) 

print current_string(s)


