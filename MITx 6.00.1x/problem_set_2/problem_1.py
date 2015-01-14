balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

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

monthlyStatement(balance, annualInterestRate, monthlyPaymentRate)
