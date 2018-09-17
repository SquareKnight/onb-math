"""Special Pythagorean triplet
n;Sum of a+b+c;int;1000
#Pythagoras
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def attempt_1(n):
    for a in range(1, n):
        for b in range(a+1, n):
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0 and a+b+c == n:
                return a*b*c


def attempt_2(x):
    m, n = 20, 20
    a, b, c = 0, 0, 0
    while a+b+c != x:
        a, b, c = max(m, n)**2 - min(m, n)**2, 2*m*n, m**2 + n**2
        if a+b+c > x:
            m-=1
        if a+b+c < x:
            n+=1
    return a*b*c

def run(n):
    #return attempt_1(n)
    return attempt_2(n)


if __name__ == '__main__':
    print(run(1000))
