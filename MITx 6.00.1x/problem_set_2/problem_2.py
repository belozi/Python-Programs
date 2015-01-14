balance = 3329
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
    monthlyPaymentRate = z
    count = 0
    total = 0
    while count < 12:
        payment = balance * monthlyPaymentRate
        ub = (balance - payment) + ((balance - payment) * rate(annualInterestRate))
        balance = ub
        total += payment
        count += 1
        print ("Month: " + str(count) + "\nMinimum monthly payment: " + "%.2f" % (payment) + "\nRemaining balance: " + "%.2f" % ub)
    print ("Total paid: " + "%.2f" % total + "\nRemaining balance: " + "%.2f" % ub)

def lowestPayment(x, y):
    payment = 0
    while balance > 0:
        payment += 10
        monthlyStatement(x, y, payment)
    print payment

lowestPayment(balance, annualInterestRate)
