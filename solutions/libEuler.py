import math

_primes = []

def _sieve_of_eratosthenes(upper):
    print("sieve")
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
