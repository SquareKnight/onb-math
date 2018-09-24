"""Summation of primes
n;Upper limit;int;2000000
#Primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import solutions.libEuler as e


def attempt_1(n):
    primes = e.primes_list(1, n)
    return sum(primes)

def run(n):
    return attempt_1(n)


if __name__ == '__main__':
    print(run(2000000))
