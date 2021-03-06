"""10001st prime
x;the x'th prime;int;10001
#Primes
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import solutions.libEuler as e


def attempt_1(n):
    upper = 100000
    e._sieve_of_eratosthenes(upper)
    while len(e._primes) < n:
        upper += 10000
        e._sieve_of_eratosthenes(upper)

    return e._primes[n-1]

def attempt_2(n):
    upper = 100000
    primes = e.primes_list(1, upper)
    while len(primes) < n:
        upper += 10000
        primes = e.primes_list(1, upper)

    return primes[n-1]

def run(n):
    return attempt_2(n)


if __name__ == '__main__':
    print(run(10001))
