import math

__boolean_primes_register = []
_primes = []


def _sieve_of_eratosthenes(upper):
    candidates = [False, False, True]
    second_list = [True] * (upper - 2)
    candidates.extend(second_list)

    for i in range(0, upper + 1):
        if candidates[i] == False:
            continue

        for multiple in range(i*i, upper + 1, i):
            candidates[multiple] = False

    global _primes
    _primes = []
    for i, b in enumerate(candidates):
        if b:
            _primes.append(i)


def _sieve_persistent(upper):
    global _primes, __boolean_primes_register

    # see how many numbers we've sieved through before
    primes_sieved = 0 if __boolean_primes_register == [] else len(__boolean_primes_register)

    # If we've already checked everything up to Upper, then quit the function
    if primes_sieved >= upper + 1:
        return

    # if not, extend the BPR
    if __boolean_primes_register == []:
        __boolean_primes_register = [False, False, True]
        second_list = [True] * (upper - 2)
        __boolean_primes_register.extend(second_list)
    else:
        __boolean_primes_register.extend([True]*(1 + upper - primes_sieved))

    # take into account all the primes we've found before
    for p in _primes:
        # check to see where the first multiple lies in the range (already solved) ... (upper bound):
        mod = primes_sieved % p
        lower = primes_sieved - mod + (p if mod > 0 else 0)
        if p*p > upper:
            break

        for multiple in range(max(lower, p*p), upper + 1, p):
            __boolean_primes_register[multiple] = False

    # then apply the regular Sieve of E.
    for i in range(primes_sieved, upper + 1):
        if not __boolean_primes_register[i]:
            continue

        if i*i > upper:
            break

        for multiple in range(i*i, upper + 1, i):
            __boolean_primes_register[multiple] = False

    # now add all the new-found primes to _primes
    for i in range(primes_sieved, upper + 1):
        if __boolean_primes_register[i]:
            _primes.append(i)


print("setup")

import random
import time as tx

results = []
rnds = []
for x in range(50):
    rnds.append(random.randint(0, 5 * 10**5))
rnds = sorted((rnds))

print(min(rnds), max(rnds))

print("Sieve 1")
_primes = []
__boolean_primes_register = []
t = tx.time()
for i, r in enumerate(rnds):
    #print("Case ", i, r)
    _sieve_of_eratosthenes(r)
results.append("Original function- # Primes: {0}\t\tHighest prime: {1}\t\tSeconds: {2}".format(len(_primes), _primes[-1],tx.time()-t))

print("Sieve 2")
_primes = []
__boolean_primes_register = []
t = tx.time()
for i, r in enumerate(rnds):
    #print("Case ", i, r)
    _sieve_persistent(r)
results.append("New and improved - # Primes: {0}\t\tHighest prime: {1}\t\tSeconds: {2}".format(len(_primes), _primes[-1],tx.time()-t))


for rs in results:
    print(rs)
