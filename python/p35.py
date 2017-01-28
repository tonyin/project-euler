#!/usr/bin/env python

import time
import math


# Problem:
# How many circular primes are there below one million?

def sieve_erat(ub):
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

def circs(n, orig):
    n2 = str(n)[-1] + str(n)[:-1]
    if n2 == str(orig): return [int(n2)]
    else:
        return [int(n2)] + circs(n2, orig)

def main():
    ub = 1000000 # upper bound
    primes = sieve_erat(ub)
    c = 0
    for i in range(1, ub):
        if primes[i] == True:
            check = circs(i, i)
            if all(primes[j] == True for j in check):
                c += 1
    print(c)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
