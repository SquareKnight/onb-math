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


def int_to_list(i):
    return [int(c) for c in str(abs(i))]


for x in (1, 10, 11, -10, 123, 145, 9999):
    print(x, int_to_list(x))