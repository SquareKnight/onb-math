import math

def prime_sieve(n):
    nums = [False, False, True]
    nums.extend([True] * (n-2))

    for x in range(n+1):
        if not nums[x]:
            continue

        y = x*2
        print(x, y)
        nums[y:n+1:x] = [False] * math.floor(n/x-1)
    return(nums)


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    primes = [2]

    for p in range(3, n + 1, 2):
        if is_prime[p]:
            primes.append(p)

            for multiple in range(p * p, n + 1, p + p):
                is_prime[multiple] = False

    return primes


if __name__ == '__main__':
    l = prime_sieve(1000)
    for i, x in enumerate(l):
        if l[i]:
            print(i, x)
