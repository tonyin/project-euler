#!venv/bin/python

import time

DATA = 'data/'


def main():

	# Read, scrub, and sort names
	names = []
	with open(DATA + 'p022_names.txt', 'r') as names_raw:
		names = names_raw.read().replace('"','').split(',')
	names.sort()

	# Define helper function for calculating apha value
	def alpha_value(name): return sum([ord(char) - 96 for char in name.lower()])

	print sum([alpha_value(name)*(names.index(name)+1) for name in names])

if __name__ == '__main__':
	start = time.time()
	main()
	print 'Program runtime: {0:.3f}s'.format(time.time() - start)
