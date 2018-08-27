"""Sum square difference
limit;Numbers from 1 to n;int;100
#squares
The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def attempt_1(n):
    a = 0   # sum of squares
    b = 0   # square of sums
    for i in range(1, n+1):
        a += i**2
        b += i

    return (b**2) - a

def run(n):
    return attempt_1(n)


if __name__ == '__main__':
    print(run(100))
