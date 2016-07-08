#!venv/bin/python

import time


def main():
    curr = 1
    prev = 1
    idx = 2
    while len(str(curr)) < 1000:
        tmp = curr
        curr = curr + prev
        prev = tmp
        idx += 1
    print idx

if __name__ == '__main__':
	start = time.time()
	main()
	print 'Program runtime: {0:.3f}s'.format(time.time() - start)
