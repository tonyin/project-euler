#!/usr/bin/env python

import time
import itertools


# Problem:
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# Two possible combinations:
# 1 x 4 = 4
# 2 x 3 = 4

def main():
    digits = list(range(1, 10))
    pandigitals = []
    for i in list(itertools.permutations(digits)):
        if i[0] * int(str(i[1]) + str(i[2]) + str(i[3]) + str(i[4])) == int(str(i[5]) + str(i[6]) + str(i[7]) + str(i[8])):
            pandigitals.append(int(str(i[5]) + str(i[6]) + str(i[7]) + str(i[8])))
        if int(str(i[0]) + str(i[1])) * int(str(i[2]) + str(i[3]) + str(i[4])) == int(str(i[5]) + str(i[6]) + str(i[7]) + str(i[8])):
            pandigitals.append(int(str(i[5]) + str(i[6]) + str(i[7]) + str(i[8])))

    print(sum(set(pandigitals)))

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
