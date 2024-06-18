import math
def isPrime(n):
    for x in range(2, math.ceil(n**0.5)):
        if n % x == 0:
            print(x)

isPrime(10)
