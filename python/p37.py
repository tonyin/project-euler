#!/usr/bin/env python

import time


# Problem:
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

def sieve_era(ub):
    primes = [True for i in range(1, ub+1)]
    primes[1] = False
    for i in range(2, ub):
        if primes[i] == False: continue
        primes[i] = True
        if i**2 < ub:
            for j in range(i**2, ub, i):
                if j % i == 0:
                    primes[j] = False
    return primes

def truncatable(n, primes):
    if primes[n] == False: return False
    for i in range(1, len(str(n))):
        if primes[int(str(n)[i:])] == False:
            return False
        if primes[int(str(n)[:-i])] == False:
            return False
    return True

def main():
    ub = 1000000 # upper bound
    primes = sieve_era(ub)
    print(sum([i for i in range(10, ub) if truncatable(i, primes)]))

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
