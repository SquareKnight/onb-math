"""Sum all the multiples of 3 and 5 below 1000
n;upper bound;int
#basics

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def run(n):
    return attempt_1(n)


def attempt_1(n):
    x = 1
    s = 0
    while x < n:
        if x % 3 == 0:
            s += x

        if x % 5 == 0:
            s += x

        if x % 15 == 0:
            s -= x

        x += 1

    return s


def attempt_2(n):
    x = 1
    s = 0
    while x < n:
        if x % 3 == 0:
            s += x
        elif x % 5 == 0:
            s += x

        x += 1

    return s


def attempt_3(n):
    s = 0
    for x in range(1, n):
        if x % 3 == 0:
            s += x
        elif x % 5 == 0:
            s += x

    return s
