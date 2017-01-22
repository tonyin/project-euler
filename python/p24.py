#!venv/bin/python

import time
from math import factorial
import pdb

NTH = 1000000
DIGITS = [0,1,2,3,4,5,6,7,8,9]

def find_nth(result, idx_total, idx_digit, possible):
    if len(possible) == 1:
        return result + str(possible[0])
    elif idx_digit == len(possible) - 1:
        return find_nth(result + str(possible[-1]), idx_total, 0, possible[:-1])
    elif idx_total + factorial(len(possible)-1) >= NTH:
        return find_nth(result + str(possible[idx_digit]), idx_total, 0, possible[:idx_digit] + possible[idx_digit + 1:])            
    else:
        return find_nth(result, idx_total + factorial(len(possible)-1), idx_digit + 1, possible)

def main():
	print find_nth('', 0, 0, DIGITS)

if __name__ == '__main__':
	start = time.time()
	main()
	print 'Program runtime: {0:.3f}s'.format(time.time() - start)
