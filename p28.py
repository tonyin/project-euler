#!venv/bin/python

import time


# Problem (redefined):
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

def sum_diagonal(n):
    if n < 1: return 'n needs to be > 0'
    if n == 1: return 1
    if n == 2: return sum(range(5))
    if n > 2:
        return sum_diagonal(n-2) + ((n-2)**2 + (n-1) + n**2)*2

def main():
    n = 1001
    print sum_diagonal(n)

if __name__ == '__main__':
	start = time.time()
	main()
	print 'Program runtime: {0:.3f}s'.format(time.time() - start)
