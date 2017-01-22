#!venv/bin/python

import time


# Problem (redefined):
# Find max(x) such that (n-x)^2 + (n-x) + 41 in quadratic form n^2 + an + b has |a| < 1000 and |b| < 1000

def main():
    
    a = lambda x: -2*x+1
    b = lambda x: x**2-x+41

    print reduce(lambda a, b: a*b,
        [(a(x), b(x)) for x in range(40) if a(x) < 1000 and b(x) < 1000][-1])

if __name__ == '__main__':
	start = time.time()
	main()
	print 'Program runtime: {0:.3f}s'.format(time.time() - start)
