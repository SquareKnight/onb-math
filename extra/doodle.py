cache={}

def collatz(n):
    if n == 1:
        cache[1] = 1

    if n not in cache:
        if n % 2:   # > 0
            cache[n] = collatz(n*3+1) + 1
        else:
            cache[n] = collatz(n/2) + 1

    return cache[n]


for i in range(1,1000000):
    collatz(i)

print(max(cache, key=cache.get))

print()
for i in range(1, 1001):
    print(i, cache[i])