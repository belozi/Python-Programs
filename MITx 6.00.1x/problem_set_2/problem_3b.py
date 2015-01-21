balance = 999999
annualInterestRate = .18

lowerBound = balance / 12
upperBound = (balance * ( 1 + .18)) / 12
payment = (upperBound + lowerBound) / 2


def guessPayment(l, u):

    lower = l
    upper = u
    return (lower + upper) / 2
    
def monthlyStatement(x, y, z):
    balance = x
    annualInterestRate = y
    payment = z
    count = 0
    total = 0
    while count < 12:
        ub = (balance - payment) + ((balance - payment) * (annualInterestRate / 12))
        balance = ub
        total += payment
        count += 1
    return balance
  
check = monthlyStatement(balance, annualInterestRate, payment)

counter = 0
while  counter < 25:  
    check = monthlyStatement(balance, annualInterestRate, payment)
    if check >= 0 and check < .01:
        print ("Lowest Payment: " + "%.02f" %payment)
        break
    elif check > 0:
        counter += 1
        lowerBound = payment
        payment = guessPayment(lowerBound, upperBound)
    else:
        counter += 1
        upperBound = payment
        payment = guessPayment(lowerBound, upperBound)

        


