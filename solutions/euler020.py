"""Factorial digit sum
n;Factorial;int;100
#Digits
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import solutions.libEuler as e
import math


def attempt_2(n):
    prod = math.factorial(n)
    return sum(list(map(int, str(prod))))


def attempt_1(n):
    f = list(range(2, n+1))
    prod = e.product_of_list(f)
    return sum(list(map(int, str(prod))))


def run(n):
    return attempt_2(n)


if __name__ == '__main__':
    print(run(10))