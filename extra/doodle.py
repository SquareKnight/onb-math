def probs_31():

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    ways_to_make_x = dict()
    for i in range(1, target+1):
        w = []
        for c in coins:
            y = i - c
            if y < 0:
                break

            if y == 0:
                w.append([c])
                break

            if y > 0:
                w_prev = ways_to_make_x[y]
                for wp in w_prev:
                    w.append(sorted([c] + list(wp)))

        w = tuple([tuple(l) for l in w])
        ways_to_make_x[i] = set(tuple(w))

    print(len(ways_to_make_x[target]))

"""

n**2    +   an    +    b

when n == 0:    0**2 + 0a + b   ==> b needs to be prime, also
                                    b needs to be positive as we don't regard negative numbers to be prime
        ==> a can be anywhere from -999 to 1000, but
        ==> if a < 0, b >= |a|, because let n==1, 1**2 + -a + b > 0 only if b 'outweighs' a.
        
let n == 1: a + b + 1   ==> the result needs to be a prime, so a+b+1's prime factors list can only be len()==1
                                
                                   
"""
import solutions.libEuler as e
import time as t

def get_next_quadratic(a, b):
    n = 0
    while True:
        yield n**2 + a*n + b
        n += 1

# 75 secs
# 46 secs when limiting a to -b
# 29 secs with (a+b+1) == prime
# 25 secs with prime factors (x) function quitting early if x is prime

def euler_027():
    b_primes = e.primes_list(0, 1000)
    longest_series = (0, 0, 0)


    for b in reversed(b_primes):
        print(b)
        if b < longest_series[0]:
            break
        for a in range(-b, 1000):
            if len(e.prime_factors(a+b+1)) != 1:
                continue

            this_series = 0
            f = get_next_quadratic(a, b)
            fn = next(f)

            while len(e.prime_factors(fn)) == 1:
                this_series += 1
                fn = next(f)

            if this_series > longest_series[0]:
                longest_series = (this_series, a, b)

    return longest_series

import math

def euler_027_2():
    def isPrime(n):
        if n % 2 == 0 or n < 2:
            return False
        for test in range(3, int(math.sqrt(n)+1), 2):
            if n % test == 0:
                return False
        return True

    def consec_primes(a,b):
        n = 0
        while isPrime(n**2 + a*n + b):
            n+=1
        return n

    b_primes = e.primes_list(0, 1000)
    longest_series = (0, 0, 0)

    for b in reversed(b_primes):
        print(b)
        if b < longest_series[0]:
            break
        for a in range(-b, 1000):
            if len(e.prime_factors(a+b+1)) > 1:
                continue

            this_series = consec_primes(a, b)

            if this_series > longest_series[0]:
                longest_series = (this_series, a, b)

    return longest_series


tx = t.time()
l = euler_027()
print(l, l[1] * l[2])
print(t.time() - tx)
print(sum(e._sieve_ops), e._sieve_ops)