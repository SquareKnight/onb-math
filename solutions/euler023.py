"""Non-abundant sums
n;upper bound;int;28123
#divisor
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this
sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less
than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import solutions.libEuler as e


def attempt_1(n):
    abundants = []
    for i in range(1, n+1):
        d = e.divisors(i)
        if sum(d) > i:
            abundants.append(i)

    sums_of_abundants = []
    for x in range(len(abundants)):
        for y in range(x, len(abundants)):
            q = abundants[x] + abundants[y]
            if q > n: break
            sums_of_abundants.append(q)

    sums_of_abundants = set(sums_of_abundants)

    non_sums = [a for a in range(n+1) if a not in sums_of_abundants]
    return sum(non_sums)

def run(n):
    return attempt_1(n)


if __name__ == '__main__':
    print(run(28123))