#!/usr/bin/env python

# Problem:
# Find largest n-digit pandigital (number that contains digits 1 to n exactly once) prime?

import time
import itertools

def sieve_eratosthenes(ub):
    assert(ub >= 1)
    primes = [True for i in range(1, ub+1)]
    primes[1] = False
    for i in range(2, ub):
        if primes[i] == False: continue
        if i**2 < ub:
            for j in range(i**2, ub, i):
                if j % i == 0:
                    primes[j] = False
    return primes

def main():
    # Build primes from Sieve of Eratosthenes
    # Largest possible n-digital pandigital is 987,654,321; building primes to 1,000,000,000 is too intensive
    # Fortunately we can ignore any 9-digit pandigital because it is divisable by 3 (sum of digits % 3 == 0)
    # Same with 8-digit. So max we need to check is 7,654,321
    N = 8000000

    primes = sieve_eratosthenes(N)
    digits = [i for i in range(1,int(len(str(N))+1))]
    permutations = [int(''.join([str(i) for i in n])) for n in list(itertools.permutations(digits))]

    max_n = 0
    for n in permutations:
        if primes[n] and n > max_n:
            max_n = n
    
    print(max_n)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
