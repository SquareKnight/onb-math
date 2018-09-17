import math

def x1():
    i = 0
    for a in range(1, 1000):
        for b in range(a, 1000):
            i += 1
            c = math.sqrt(a**2 + b**2)
            #print(a, b, c)
            if c%1==0 and a+b+c == 1000:
                return (a*b*c, i)


def x2():
    i = 0
    m = 10
    n = 10
    a, b, c = 0, 0, 0
    while a+b+c != 1000:
        i += 1
        a, b, c = max(m, n)**2 - min(m, n)**2, 2*m*n, m**2 + n**2
        #print(a, b, c)
        if a+b+c > 1000:
            m-=1
        elif a+b+c < 1000:
            n+=1

    return (a*b*c, i)


import time as tx

t = tx.time()
print(x1())
print(tx.time() - t)

t = tx.time()
print(x2())
print(tx.time() - t)
