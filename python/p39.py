#!/usr/bin/env python

import time
import math


# Problem:
# What value of p <= 1000 is there a maximal number of solutions for p as perimeter of right triangle with integer sides?

def right_triangle(a, b, c):
    if (a+b<=c) or (a+c<=b) or (b+c<=a):
        return False
    return a**2+b**2 == c**2

def main():
    P = 1000

    max_solutions = 0
    max_p = 3
    for p in range(3,P+1):
        solutions = 0
        for a in range(1,math.ceil((p+1)/3)):
            for b in range(a,math.ceil((p+1)/2)):
                c = p-a-b
                if right_triangle(a,b,c):
                    solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            max_p = p
    
    print(max_p)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
