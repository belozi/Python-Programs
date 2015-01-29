x = "Write an iterative function"

def lenRecur(aStr):
    def count(x):
        x = x.lower()
        if not x:
            return 0
        return (1 if x[0] in "abcdefghijklmnopqrstuvwxyz" else 0) + count(x[1:])
    return count(x)
            

print lenRecur(x)
                 
