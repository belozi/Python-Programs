def genPrimes():
    number = 2
    primes = [2]
    yield number
    while True:
        prime = True
        number += 1
        for x in primes:
            if number % x != 0:
                continue
            else:
                prime = False
        if prime == True:
            primes.append(number)
            yield number
                    

