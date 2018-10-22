def attempt_1(m, n):
    row = [1] * (n + 1)
    for i in range(m):
        for j in range(1, n+1):
            row[j] = row[j] + row[j-1]
        #print(row)
    return row[n]


import math


def attempt_2(m, n):
    #if m < n:
    #    m, n = n, m
    return math.factorial(m+n) // (math.factorial(m) * math.factorial(n))

side = 1000

import time as tx
t = tx.time()
print(attempt_1(2, 2), attempt_1(2, 3), attempt_1(3, 2), attempt_1(3, 3))
print(attempt_1(side, side))
print(tx.time() - t)

t = tx.time()
print(attempt_2(2, 2), attempt_2(2, 3), attempt_2(3, 2), attempt_2(3, 3))
print(attempt_2(side, side))
print(tx.time() - t)