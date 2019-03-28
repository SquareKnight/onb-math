"""Digit factorials

#factorial
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import solutions.libEuler as e
from math import factorial


def attempt_1():
    r = 0
    for i in range(10, 2540160):
        s_f = 0
        for d in e.int_to_list(i):
            s_f += factorial(d)
        if s_f == i:
            r += i

    return r


def attempt_2():
    r = 0
    factorials = [factorial(i) for i in range(10)]

    for i in range(10, 2540160):
        s_f = 0
        for d in e.int_to_list(i):
            s_f += factorials[d]

        if s_f == i:
            r += i

    return r


def attempt_3():
    r = 0
    for a in range(10, 2540160):
        ld = sum([factorial(int(c)) for c in str(a)])
        if ld == a:
            print(a)
            r += a
    return r

def run():
    return attempt_3()


if __name__ == '__main__':
    print(run())
