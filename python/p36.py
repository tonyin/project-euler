#!/usr/bin/env python

import time


# Problem:
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def is_palindrome(n):
    if n < 1: return False
    elif n < 10: return True
    elif len(str(n)) % 2 == 0:
        for i in range(int((len(str(n))/2))):
            if str(n)[i] != str(n)[-i-1]: return False
        return True
    else:
        for i in range(int((len(str(n))-1)/2)):
            if str(n)[i] != str(n)[-i-1]: return False
        return True

def base_10to2(n):
    d = 0
    while 2**(d+1) <= n:
        d += 1
    b2 = []
    for i in sorted(range(d+1), reverse=True):
        if 2**i <= n:
            b2.append(1)
            n = n - 2**i
        else:
            b2.append(0)
    return int(''.join([str(i) for i in b2]))

def main():
    ub = 1000000 # upper bound
    print(sum([i for i in range(ub) if is_palindrome(i) and is_palindrome(base_10to2(i))]))

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
