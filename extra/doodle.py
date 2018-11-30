import math

def divisors(n):
    n = abs(n)
    if n <= 1: return [0]
    r = []
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            r.extend([i, n//i])
    return set(r)


def amicable_1(n):
    amicable = []
    l = [*range(1, n+1)]
    for i in l:
        a = i
        x = sum(divisors(a))
        b = x
        y = sum(divisors(b))

        if x == y:
            print(a, x, b, y)

    return amicable


l = amicable_1(10000)
print(l)
print(sum(l))


"""
s = []
for q in range(2, 10001):
    s.extend(divisors(q))
print(sum(s))
"""