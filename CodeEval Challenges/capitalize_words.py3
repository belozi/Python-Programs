import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    result = test.title()
    print result
test_cases.close()
