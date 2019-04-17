"""Double-base palindromes
limit;Test to number;int;1000000
#palindrome
The decimal number, 585 = 0b1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def attempt_1(limit):
    r = 0
    for i in range(1, limit, 2):
        str_i = str(i)
        if str_i == str_i[::-1]:
            bin_i = bin(i)[2::]
            if bin_i == bin_i[::-1]:
                r += i
    return r


def make_palindrome(n, is_odd):
    r = n
    if is_odd:
        n = n // 10

    while n > 0:
        a = n % 10
        r = (r*10) + a
        n = n // 10
    return r


def attempt_2(limit):
    r = 0

    for isodd in [True, False]:
        q = 1
        p = make_palindrome(q, isodd)
        while p <= limit:
            bin_i = bin(p)[2::]
            if bin_i == bin_i[::-1]:
                r += p
            q += 1
            p = make_palindrome(q, isodd)

    return r


def run(limit):
    #return attempt_1(limit)
    return attempt_2(limit)


if __name__ == '__main__':
    print(run(100))
