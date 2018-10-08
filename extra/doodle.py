import solutions.libEuler as e
from math import sqrt, ceil

def countdiv_suggested(x):
    pf = e.prime_factors(x)
    pf_ex = dict()
    pf_keys = set(pf)
    for k in pf_keys:
        pf_ex[k] = pf.count(k) + 1

    nums = [p[1] for p in pf_ex.items()]
    return e.product_of_list(nums)

def countdiv_combi(x):
    r = 0
    divs = []
    for i in range(1, ceil(sqrt(x))+1):
        if (x / i) % 1 == 0:
            r += 1 if i == sqrt(x) else 2
            divs.extend([i, x/i])
    return (r, sorted(divs))


n = 76576500
print(countdiv_suggested(n))
print(countdiv_combi(n))
