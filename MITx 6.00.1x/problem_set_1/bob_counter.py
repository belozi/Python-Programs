s = 'azcbobobegghakl'

def wordCounter(x):
    count = 0
    pos = 0
    while pos <= len(s) - 1:
        s.find(x, pos, len(s) - 1)
        if s.find(x, pos) == -1:
            break
        count += 1
        pos = s.find(x, pos) + 1
    return count

print("Number of times bob occurs is: " + str(wordCounter('bob')))




    
