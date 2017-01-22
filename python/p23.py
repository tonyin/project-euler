#!venv/bin/python

import time

# Plan:
# divisorize
# calc abundanciness
# iterate through abundants to calc possibles
# remove possibles from range 28123
# return sum

from math import sqrt, ceil
MIN = 12
MAX = 28123

def get_proper_divisors(n):
    proper_divisors = []
    for i in range(1, int(ceil(sqrt(n)))+1):
        if n % i == 0:
            proper_divisors.append(i)
            proper_divisors.append(n/i)
    proper_divisors.remove(n)
    return list(set(proper_divisors))


def main():

	# Calculate all of the abundant numbers
	abundants = []
	for i in range(MIN, MAX+1):
	    if sum(get_proper_divisors(i)) > i:
	        abundants.append(i)
	abundants.sort()

	# Calculate all of the possible abundant sums
	possibles = []
	for i in range(len(abundants)):
	    if abundants[i]*2 > MAX: break
	    for j in range(len(abundants)):
	        j += i
	        if j == len(abundants): break
	        possible = abundants[i] + abundants[j]
	        possibles.append(possible)

	print sum(set(range(MAX+1)).difference(set(possibles)))

if __name__ == '__main__':
	start = time.time()
	main()
	print 'Program runtime: {0:.3f}s'.format(time.time() - start)
