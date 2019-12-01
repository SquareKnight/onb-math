"""Champernowne's constant
limit;last significant digit;int;1000000
#Champernowne
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


def attempt_1(limit):
    digs = [limit]
    while limit != 1:
        limit /= 10
        digs.append(int(limit))

    champ, i = "0", 1
    while len(champ) <= max(digs):
        champ += str(i)
        i += 1

    p = 1
    for d in digs:
        p *= int(champ[d])

    return p


def run(limit):
    return attempt_1(limit)


if __name__ == '__main__':
    print(run(1000000))
