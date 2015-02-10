import sys

test_cases = open(sys.argv[1], 'r')
lines = test_cases.readlines()
for line in lines:
    words = line.split()
    sentence = []
    for word in words:
        sentence.append(word[0].upper() + word[1:])
    print ' '.join(sentence)
    


