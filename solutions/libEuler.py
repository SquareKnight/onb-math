import math

__boolean_primes_register = [False, False, True]
_primes = [2]
_sieve_ops = []


def _sieve_of_eratosthenes(upper):
    if upper < 1:
        return
    global _primes, __boolean_primes_register
    upper = int(upper)
    # see how many numbers we've sieved through before
    primes_sieved = len(__boolean_primes_register)

    # If we've already checked everything up to Upper, then quit the function
    if primes_sieved > upper:
        return

    # if not, extend the BPR
    __boolean_primes_register.extend([True]*(1 + upper - primes_sieved))
    _sieve_ops.append(1 + upper - primes_sieved)

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

    #print(upper, [(i, x) for i, x in enumerate(__boolean_primes_register)], _primes)


def is_prime(n):
    if n < 2 or (n>2 and n % 2 == 0):
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False

    return True


def prime_factors(n):
    """
    Returns all prime factors of n
    :param n: The number to get the prime factors of
    :return: list of prime factors, with duplicates if applicable: 4 -> [2, 2]
    """
    global _primes
    #pf = [1]
    pf = []
    n = abs(n)
    if n < 2:
        return []
    lim = math.ceil(math.sqrt(n))
    _sieve_of_eratosthenes(lim)

    # Use every prime, in order from 2 to (at least) lim to deconstruct n
    for p in primes_list(1, lim):
        if n == 1:
            break   # n has been fully deconstructed
        while n % p == 0:
            # if n can be divided by prime p, do so, and add p to the list of prime factors
            # This is in a while-loop because the same prime might divide n multiple times: 8 / 2 = 4, /2 = 2, /2 = 1
            pf.append(p)
            n = n / p

    # if the above loop didn't fully deconstruct n, then whatever remains is itself prime too
    if n > 1:
        pf.append(n)


    #if len(pf) > 1:
    #    pf = pf[1::]
    _sieve_of_eratosthenes(pf[-1])
    return pf


def primes_list(lower, upper, overshoot_upperbound = False):
    """
    Returns a list with all primes between lower and upper bound
    :param lower: Lower bound
    :param upper: Upper bound
    :param overshoot_upperbound: If this is true, the last boolean will be bigger than upper, ie upper will be inside of the range.
    :return: list
    """
    if upper < lower:
        lower, upper = upper, lower
    _sieve_of_eratosthenes(upper)
    primes = [p for p in _primes if p >= lower and p <= upper]
    if overshoot_upperbound and primes[-1] < upper:
        tmp = upper
        while _primes[-1] == primes[-1]:
            tmp += 1
            _sieve_of_eratosthenes(tmp)
        x = _primes.index(primes[-1]) + 1
        primes.append(_primes[x])
    return primes


def product_of_list(lst):
    lst = list(map(int, lst))
    if 0 in lst: return 0

    p = 1
    for x in lst:
        p *= x
    return p


def divisors(n, exclude_n=True):
    """
    Given n, returns a list of all divisors op n
    :param n:           Number to divide
    :param exclude_n:   Flag to signify if n itself should be on the list
    :return:            List of divisors, or [] for n < 1
    """
    if n < 1: return []
    r = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            r.append(i)
            r.append(n//i)

    if exclude_n:
        r.remove(n)
    return set(r)


def permutate(lst, index):
    """
    Given a list and an index, it will return the N'th lexicographically ordered permutation
    :param lst:     the collection of elements to arrange
    :param index:   the index into the permutation catalog
    :return:        a list with the requested permutation
    """
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return lst

    lst = (sorted(lst))

    def inner_permutate(l, i):
        if len(l) == 2:
            x = i % 2
            return [l[x], l[1-x]]

        f = math.factorial(len(l))
        i = int(i) % f

        g = math.factorial(len(l) - 1)
        SLOT = int(i / g)
        return [l.pop(SLOT)] + inner_permutate(l, i)

    return inner_permutate(lst, index)


def simplify_fraction(n, d):
    """
    Simplifies fractions by determining common prime factors and removing those on both the
    numerator and the denominator.
    :param n: numerator
    :param d: denominator
    :return: new_numerator, new_denominator
    """
    pf_n, pf_d = prime_factors(n), prime_factors(d)
    commons = []
    for pf in set(pf_n + pf_d):
        commons.extend([pf] * min(pf_n.count(pf), pf_d.count(pf)))

    for pf in commons:
        pf_n.remove(pf)
        pf_d.remove(pf)

    return product_of_list(pf_n), product_of_list(pf_d)


def int_to_list(i):
    """
    Converts an integer to a list of digits
    :param i: integer
    :return: yields the digits
    """
    for c in str(abs(i)):
        yield int(c)