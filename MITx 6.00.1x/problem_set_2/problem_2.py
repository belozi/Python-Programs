balance = 3926
annualInterestRate = .20

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

def lowestPayment(x, y):
    payment = 0
    while monthlyStatement(x, y, payment) > 0:
        payment += 10
        monthlyStatement(x, y, payment)
    return ("Lowest Payment: " + str(payment))

print lowestPayment(balance, annualInterestRate)
#monthlyStatement(balance, annualInterestRate, 310)
