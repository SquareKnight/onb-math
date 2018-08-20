"""Smallest multiple
n;Numbers from 1 to n;int
#multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import solutions.libEuler as e

def attempt_1(n):
    # brute force
    i = n-1
    while True:
        i += 1
        hit = True
        for x in range(1, n+1):
            if i % x != 0:
                hit = False
                break
        if hit:
            break

    return i

def attempt_2():
    n = 20
    i = 2520 - 20
    while True:
        i += 20
        hit = True
        for x in [20, 19, 18, 17, 16, 14, 13, 11]:
            if i % x != 0:
                hit = False
                break
        if hit:
            break

    return i

def attempt_3(n):
    d_pfcount = {}
    for i in range(2, n+1):
        pf = e.prime_factors(i)
        uniq = set(pf)
        for u in uniq:
            c = pf.count(u)
            if u not in d_pfcount:
                d_pfcount[u] = c
            else:
                d_pfcount[u] = max(c, d_pfcount[u])

    product = 1
    for k in d_pfcount:
        product = product * (k ** d_pfcount[k])
    return product

def run(n):
    #return attempt_1(n)
    #return attempt_2()
    return attempt_3(n)

if __name__ == '__main__':
    print(run(10))
