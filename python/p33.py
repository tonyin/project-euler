#!/usr/bin/env python

import time


# Problem:
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def prod(l):
    if len(l) > 1:
        return l[0] * prod(l[1:])
    else:
        return l[0]

def main():
    curios = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j: continue
            n1 = int(str(i)+str(j))
            
            for k in range(1, 10):
                for l in range(1, 10):
                    if i == j: continue
                    n2 = int(str(k)+str(l))
                    if n1 >= n2: continue
                    
                    if i == k and n1/n2 == j/l:
                        curios.append((n1, n2))
                    if i == l and n1/n2 == j/k:
                        curios.append((n1, n2))
                    if j == k and n1/n2 == i/l:
                        curios.append((n1, n2))
                    if j == l and n1/n2 == i/k:
                        curios.append((n1, n2))
    
    n = prod([n for (n,d) in curios])
    d = prod([d for (n,d) in curios])

    print(n/d)

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
