#!/usr/bin/env python

# Problem:
# Number of words where word's alpha value is a triangle number?

import time
import math

def alpha_value(word):
    return sum([ord(char) - 96 for char in word.lower()])

def main():
    with open('data/p042_words.txt', 'r') as raw:
        words = raw.read().replace('"','').lower().split(',')

    word_max = max([alpha_value(w) for w in words])
    triangles = []
    n = 1
    while math.floor(n*(n+1)/2) < word_max:
        triangles.append(int(n*(n+1)/2))
        n += 1
    
    print(len([w for w in words if alpha_value(w) in triangles]))

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
