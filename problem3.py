# what is the largest prime factor of the number 600851475143?
from sympy import primerange, isprime

def largest_prime_factor(n):
    if isprime(n):
        return n
    else:
        largestPrime = 1
        for p in primerange(1, n):
            if n % p == 0:
                largestPrime = p
                print('Current largestPrime:', largestPrime)
        return largestPrime

print(largest_prime_factor(600851475143))