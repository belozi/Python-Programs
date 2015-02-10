import sys
import math

#test_cases = open(sys.argv[1], 'r')
test_cases = open('test.txt', 'r')
lines = test_cases.readlines()
for set in lines:
    pair = set.split(",")
    x = int(pair[0])
    y = int(pair[1].rstrip())
    z = 1
    while x > y:
        y = 2**(z )
        z += 1
    print y


