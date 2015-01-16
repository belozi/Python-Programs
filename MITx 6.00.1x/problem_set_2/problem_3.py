balance = 999999
annualInterestRate = .18

"""
def minimumPayment(x, y):
    balance = x
    annualInterestRate = y
    monthlyInterestRate = annualInterestRate/12
    lowestPayment = balance * ((monthlyInterestRate * (1 + monthlyInterestRate)**12) / ((1 + monthlyInterestRate)**12 - 1))
    return("Lowest Payment: " "%.2f" %lowestPayment)

print minimumPayment(balance, annualInterestRate)
"""
def rate(x):
    return x/12

def monthlyStatement(x, y, z):
    balance = x
    annualInterestRate = y
    payment = z
    count = 0
    total = 0
    while count < 12:
        ub = (balance - payment) + ((balance - payment) * rate(annualInterestRate))
        balance = ub
        total += payment
        count += 1
    return balance
"""
def guessPayment(x, y, z):
    if z > 0:
            lowerBound = z
    else:
            upperBound =z
    payment = (lowerBound + upperBound) / 2
    return payment
"""

def lowestPayment(x, y):
    lowerBound = x / 12
    upperBound = (x * (1 + (y / 12)**12)) / 12.0
    payment = lowerBound
    while monthlyStatement(x, y, payment) > 0:
        payment = (lowerBound + upperBound) / 2
        monthlyStatement(x, y, payment)
        lowerBound = payment
    return ("Lowest Payment: " + str(payment))


print lowestPayment(balance, annualInterestRate)
