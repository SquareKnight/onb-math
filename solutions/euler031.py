"""Coin sums
target;Amount we are trying to make;int;200
#Combination
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


def attempt_1(target):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways_to_make = {c:1 for c in range(target+1)}

    for coin in coins[1::]:
        for k in range(coin, target+1):
            ways_to_make[k] += ways_to_make[k-coin]

    return ways_to_make[target]


def run(n):
    return attempt_1(n)


if __name__ == '__main__':
    print(run(200))
