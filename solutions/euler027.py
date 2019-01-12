"""Quadratic primes
lim_a;Limit of a (absolute);int;999`lim_b;Limit of b;int;1000
#prime
Euler discovered the remarkable quadratic formula:

    n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,40**2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is
clearly divisible by 41.

The incredible formula n**2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n**2 + an + b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n=0.

"""
import solutions.libEuler as e


def attempt_1(lim_a, lim_b):
    longest_series = (0, 0, 0)
    b_prime = e.primes_list(1, lim_b, False)

    for a in range(-lim_a, lim_a + 1):
        for b in b_prime:
            if not e.is_prime(1+a+b):
                continue

            n = 0
            f = n**2 + a*n + b
            while e.is_prime(f):
                n += 1
                f = n**2 + a*n + b

            if n > longest_series[0]:
                longest_series = (n, a, b)

    print(longest_series)
    return longest_series[1] * longest_series[2]


def run(lim_a, lim_b):
    return attempt_1(lim_a, lim_b)


if __name__ == '__main__':
    print(run(1000, 1000))