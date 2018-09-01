import math

__boolean_primes_register = []
_primes = []

def _sieve_of_eratosthenes(upper):
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

def prime_factors(n):
    global _primes
    pf = [1]
    lim = math.ceil(math.sqrt(n))
    if len(_primes) == 0 or max(_primes) < lim:
        _sieve_of_eratosthenes(lim)

    for p in _primes:
        if n == 1:
            break
        while n % p == 0:
            pf.append(p)
            n = n / p

    if n > 1:
        pf.append(n)

    if len(pf) > 1:
        pf = pf[1::]
    return pf
