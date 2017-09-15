
# break operator
# prime numbers

for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        # loop fell through without finding a factor
        PrimeNumber = n
        print PrimeNumber, 'is a prime number'
