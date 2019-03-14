import solutions.libEuler as e


def simplify_fraction(numer, denom):
    f_n = e.prime_factors(numer)
    f_d = e.prime_factors(denom)

    common_fs = [f for f in f_n if f in f_d]
    while len(common_fs) > 0:
        f = common_fs.pop()
        f_n.remove(f)
        f_d.remove(f)
        common_fs = [f for f in f_n if f in f_d]

    if len(f_d) == 0:
        f_d = [1]
    if len(f_n) == 0:
        f_n = [1]

    return e.product_of_list(f_n), e.product_of_list(f_d)


def e33(l, u):
    r_d, r_n = 1, 1
    for denom in [str(s) for s in range(l, u+1)]:
        denom_int = int(denom)
        if denom_int % 10 == 0:
            # we don't want denominator 10, 20, 30 ...
            continue

        for numer in [str(s) for s in range(l, denom_int)]:
            numer_int = int(numer)

            # Now to cancel, we check for each digit of the denominator
            for c in numer:
                if c in denom:
                    # to see if we can cancel that digit in the numerator too
                    new_d = denom.replace(c, '', 1)
                    new_d_int = int(new_d)
                    new_n = numer.replace(c, '', 1)
                    new_n_int = int(new_n)

                    if (numer_int / denom_int) == new_n_int / new_d_int:
                        r_d *= new_d_int
                        r_n *= new_n_int
    print(r_n, r_d)
    a, b = simplify_fraction(r_n, r_d)
    print(a, b)
    return b


#print(probs_31(200))
#print(e32())
print(e33(10, 99))