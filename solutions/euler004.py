"""Largest palindrome product
dig;Number of digits;int;3
#Palindrome
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def attempt_1(dig):
    # brute force
    maximum = 0
    for i in range(10**(dig-1), 10**(dig)):
        for j in range(10**(dig-1), 10**(dig)):
            m = str(i * j)
            if m == m[::-1] and int(m) > maximum:
                maximum = int(m)

    return maximum

def attempt_2(dig):
    for i in range(10**(dig)-1, 10**(dig-1)-1, -1):
        for j in range(i, 10**(dig-1) - 1, -1):
            m = str(i * j)
            if m == m[::-1]:
                return m
    return None


def run(dig):
    return attempt_2(dig)


if __name__ == '__main__':
    print(run(3))
