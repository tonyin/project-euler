#!/usr/bin/env python

import time


# Problem:
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def upper_bound():
    digits = 1 # start from 1 digit
    while(1):
        ub = int(str(9)*digits)
        if ub > 9**5*digits: break
        digits += 1
    return digits

def num_fpows():
    fpows = []
    for i in range(2, 10**upper_bound()-1):
        if i == sum(int(d)**5 for d in str(i)):
            fpows.append(i)
    return sum(fpows)

def main():
    print(num_fpows())
    # print(sum([i for i in range(2, 10**upper_bound()-1) if i == sum([int(d)**5 for d in str(i)])])) # one-liner

if __name__ == '__main__':
	start = time.time()
	main()
	print('Program runtime: {0:.3f}s'.format(time.time() - start))
