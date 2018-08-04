def prime_sieve(n):
    nums = [False, False]
    nums.extend([True] * (n-1))
    print(nums)


if __name__ == '__main__':
    prime_sieve(100)