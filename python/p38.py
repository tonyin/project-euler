#!/usr/bin/env python

import time
import re


# Problem:
# Find the largest 9-digit pandigital from concatenated product of an integer and (1,2,...,n) where n > 1

def concatenate_product(n, cp='', i=1):
    if len(cp) >= 9:
        return cp
    else:
        cp += str(n*i)
        i += 1
        return concatenate_product(n, cp, i)

def is_pandigital(n, digits=list(range(1,10))):
    n = str(n)
    for i in digits:
        if str(i) in n:
            n = re.sub(str(i), '', n)
        else:
            return False
    return True

def main():
    ub = 10000 # upper bound since '9876' and 9876*2='19752' is 9 digits already
    l = 918273645 # given that concatenate_product(9) is this and pandigital

    for i in range(1,ub):
        n = concatenate_product(i)
        if len(n) > 9: continue
        elif int(n) < l: continue
        elif not is_pandigital(n): continue
        else:
            l = int(n)
    
    print(l)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
