"""Truncatable primes

#prime
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import solutions.libEuler as e


def left_trunc(n):
    s = str(n)
    for i in range(1, len(s)):
        if not e.is_prime((int(s[i::]))):
            return False
    return True


def right_trunc(n):
    s = str(n)
    for i in range(len(s) - 1, 0, -1):
        if not e.is_prime((int(s[:i:]))):
            return False
    return True


def attempt_1():
    r = []
    candidate = 11
    while len(r) < 11:
        candidate += 2
        if e.is_prime(candidate):
            if right_trunc(candidate):
                if left_trunc(candidate):
                    r.append(candidate)
    print(r)
    return sum(r)


def run():
    return attempt_1()


if __name__ == '__main__':
    print(run())
    #left_trunc(1234)
    #right_trunc((1234))
