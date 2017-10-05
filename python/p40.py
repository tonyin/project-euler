#!/usr/bin/env python

# Problem:
# Find value of d_1*d_10*d_100*d_1000*d_10000*d_100000*d_1000000 where d_n is the nth digit of irrational decimal concatenation of 0. and positive integers 1 to infinity

import time

def irrational_decimal(upper_bound):
    irr_dec = ''
    n = 1
    while len(irr_dec) < upper_bound:
        irr_dec += str(n)
        n += 1
    return irr_dec

def main():
    N = 1000000

    irr_dec = irrational_decimal(N)

    value = 1
    for i in range(7): # number of 10 powers
        n = int('1' + str(0)*i)
        value *= int(irr_dec[n-1])
    
    print(value)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
