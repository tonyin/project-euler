#!/usr/bin/env python

# Problem:
# Sum of 0-9 pandigital numbers with 3-substring sequential prime divisibility?

import time
import itertools

def main():
    digits = [i for i in range(10)]
    pandigitals = [int(''.join([str(i) for i in n])) for n in list(itertools.permutations(digits)) if n[0] != 0]
    sqp = [2, 3, 5, 7, 11, 13, 17]

    pandigitals_sqp = 0
    for n in pandigitals:
        if all([(int(str(n)[i:i+3]) % sqp[i-1]) == 0 for i in range(1, len(sqp)+1)]):
            pandigitals_sqp += n
    
    print(pandigitals_sqp)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
