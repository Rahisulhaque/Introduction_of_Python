def is_prime(x):
    isPrime = False
    if (x < 2):
       isPrime = False
    elif (x == 2):
        isPrime = True
    else:
        for n in range(2,x):
            if ( x % n) == 0:
                isPrime = False
                break
            else:
                isPrime = True
    return isPrime



number = 0
primeNumber = 0 
total = 0
while(PrimeNumber <= n):
    if (is_prime(number) == True):
        total += Number;
        primeNumber += 1


