"""Largest prime factor
n;Number to factor;int;600851475143
#Primes  #Factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import solutions.libEuler as e


def run(n):
    return max(e.prime_factors(n))


if __name__ == '__main__':
    print(run(600851475143))
