"""Digit cancelling fractions
lbound;lower bound;int;10`ubound;upper bound (incl.);int;99
#fractions
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

import solutions.libEuler as e


def cancel_digit(rem_c, s):
    l = list(s)
    l.remove(rem_c)
    return ''.join(l)


def simplify_fraction(n, d):
    pf_n, pf_d = e.prime_factors(n), e.prime_factors(d)
    commons = []
    for pf in set(pf_n + pf_d):
        commons.extend([pf] * min(pf_n.count(pf), pf_d.count(pf)))

    for pf in commons:
        pf_n.remove(pf)
        pf_d.remove(pf)

    return e.product_of_list(pf_n), e.product_of_list(pf_d)


def attempt_1(lbound, ubound):
    fractions = []

    for denom in range(lbound, ubound + 1):
        d_s = str(denom)
        if denom % 10 == 0:
            continue

        for numer in range(lbound, denom):
            n_s = str(numer)
            for c in n_s:
                if c in d_s:
                    new_n = int(cancel_digit(c, n_s))
                    new_d = int(cancel_digit(c, d_s))
                    if (new_n/new_d) == (numer / denom):
                        fractions.append((new_n, new_d))


    b_f = [1, 1]
    for f in fractions:
        b_f[0] *= f[0]
        b_f[1] *= f[1]

    b_f = simplify_fraction(*b_f)

    return b_f[1]

def run(lbound, ubound):
    return attempt_1(lbound, ubound)


if __name__ == '__main__':
    print(run(10, 99))
