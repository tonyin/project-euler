#!/usr/bin/env python

import time


# Problem:
# How many different ways can £2 be made using any number of coins?

def max_coins(value, coin):
    remainder = value % coin
    num_coins = (value - remainder) / coin
    return int(num_coins)

def coin_combos(value, coins):
    if value == 0:
        return 1
    elif len(coins) == 0:
        return 0
    elif len(coins) == 1:
        if value % coins[0] == 0:
            return 1
        else:
            return 0
    else:
        coins = sorted(coins, reverse=True)
        if coins[0] > value:
            return coin_combos(value, coins[1:])
        else:
            return sum([coin_combos(value - coins[0]*i, coins[1:]) for i in range(max_coins(value, coins[0])+1)])

def main():
    value = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    print(coin_combos(value, coins))

if __name__ == '__main__':
    start = time.time()
    main()
    print('Program runtime: {0:.3f}s'.format(time.time() - start))
