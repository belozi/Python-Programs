import sys


#test_cases = open(sys.argv[1], 'r')
test_cases = open('test.txt', 'r')
longest = None
sentences = test_cases.readlines()
for sentence in sentences:
    words = sentence.split()
    for word in words:
        if longest == None or len(word) > len(longest):
            longest = word
        else:
            continue
    print longest

