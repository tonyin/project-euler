#!/usr/bin/env python

import time
import math


# Problem:
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def curios(n):
    digits = list(str(n))
    return sum([math.factorial(int(i)) for i in digits]) == n

def main():
    ub = math.factorial(9)*7 # max digits is 7
    print(sum([i for i in range(3, ub) if curios(i)]))

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
