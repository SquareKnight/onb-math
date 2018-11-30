"""Amicable numbers
n;Upper bound;int;10000
#Divisor
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math


def divisors(n, exclude_n=True):
    if n < 1: return []
    r = []
    for i in range(1, n+1):
        if n % i == 0:
            r.append(i)

    if exclude_n:
        r.remove(n)
    return r


def divisors_2(n, exclude_n=True):
    if n < 1: return []
    r = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            r.append(i)
            r.append(n//i)

    if exclude_n:
        r.remove(n)
    return set(r)


def attempt_1(n):
    amicable = []
    for a in range(1, n):
        b = sum(divisors_2(a))
        c = sum(divisors_2(b))
        if a != b and a == c:
            amicable.append(a)

    return sum(amicable)


def run(n):
    return attempt_1(n)


if __name__ == '__main__':
    print(run(10000))
    #print(divisors_2(16))