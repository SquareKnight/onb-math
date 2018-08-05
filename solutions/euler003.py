"""Largest prime factor
n;Number to factor;int
#Prime  #Factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def prime_factors(n):
    pf = [1]
    lim = math.ceil(math.sqrt(n))
    primes = sieve_of_eratosthenes(lim)

    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            pf.append(p)
            n = n / p

    if n > 1:
        pf.append(n)

    return pf

def sieve_of_eratosthenes(upper):
    candidates = [False, False, True]
    second_list = [True] * (upper - 2)
    candidates.extend(second_list)

    for i in range(0, upper + 1):
        if candidates[i] == False:
            continue

        for multiple in range(i*i, upper + 1, i):
            candidates[multiple] = False

    primes = []
    for i, b in enumerate(candidates):
        if b:
            primes.append(i)
    return primes

def run(n):
    return max(prime_factors(n))


if __name__ == '__main__':
    print(run(600851475143))
