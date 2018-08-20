import math

def prime_factors(n):
    pf = [1]
    lim = math.ceil(math.sqrt(n))
    primes = sieve_of_eratosthenes(lim)

    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            pf.append(p)
            n = n / p

    if n > 1:
        pf.append(n)

    return pf

def sieve_of_eratosthenes(upper):
    candidates = [False, False, True]
    second_list = [True] * (upper - 2)
    candidates.extend(second_list)

    for i in range(0, upper + 1):
        if candidates[i] == False:
            continue

        for multiple in range(i*i, upper + 1, i):
            candidates[multiple] = False

    primes = []
    for i, b in enumerate(candidates):
        if b:
            primes.append(i)
    return primes


if __name__ == '__main__':
    l = sieve_of_eratosthenes(1000)
    for i, x in enumerate(l):
        if l[i]:
            print(i, x)
