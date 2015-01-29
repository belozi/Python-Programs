x = "Write an iterative function"

def lenIter(aStr):

    def charx(aStr):
        aStr = aStr.lower()
        chars = ""
        for char in aStr:
            if char in "abcdefghijklmnopqrstuvwxyz":
                chars += char
        return chars

    def count(x):
        long = 0
        for l in aStr:
            long +=1
        return long

    return count(charx(aStr))

print lenIter(x)
                 
