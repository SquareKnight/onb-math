from functools import reduce
import solutions.libEuler as e


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


def GCD(a, b):
    if a == 0:
        a = b
    if b == 0:
        return a
    while a:
        a, b = b%a, a
    return b

class primorial:

    def __init__(self, n):
        self.exponents = []
        self.prime_base = []
        self.natural = n
        self.element = self
        self.factor = 1
        # get all primes up to n, also get all oof N's prime factors
        pfs = e.prime_factors(n)
        if len(pfs) == 0:
            return
        primes = e.primes_list(1, max(pfs), False)
        self.prime_base = set(primes)
        for p in sorted(self.prime_base):
            self.exponents.append(pfs.count(p))

        # determining primordial base element
        if len(self.exponents)> 0:
            factor = reduce(GCD, self.exponents)
            if n == 25:
                print()
            if factor > 1:
                self.factor = factor
                new_pf = [exp / factor for exp in self.exponents]
                n_factors = [b**e for b, e in zip(self.prime_base, new_pf)]
                self.element = primorial(e.product_of_list(n_factors))

    def __str__(self):
        return 'primordial for {}: {}'.format(self.natural, ', '.join([str(s) for s in self.exponents]))


def indexify(total_length, number_of_fragments, current_fragment=0):
    piece = total_length / number_of_fragments
    start = piece * current_fragment
    return range(int(start), int(start+piece))


def e29(n):
    classical = len(set([a**b for a in range(2, n+1) for b in range(2, n+1)]))

    usquares = 0

    watchlist = dict()
    #first, let's see what numbers will give us duplicate ranges:
    a = 2
    while a*a <= n:
        f = 2
        while a**f <= n:
            index = a**f
            if index not in watchlist:
                watchlist[index] = f
            f += 1
        a += 1

    for a in range(2, n+1):
        if a in watchlist:
            factor = watchlist[a]
        else:
            factor = 1

        candidates = [b*factor for b in range(2, n+1)]

        for f in range(factor-1):
            for b in range(2, n+1):
                g=f+1
                if g*b in candidates:
                    candidates.remove(g*b)


        usquares += len(candidates)


    print("Classical: {}".format(classical))
    print("Primorial: {}".format(usquares))


e29(100)
