"""Pandigital multiples

#pandigit
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?
"""


def pandigital_product_maker(x):
    s = ""
    n = 1

    while len(s) < 9:
        s += str(x * n)
        n += 1

    if len(s) == 9:
        if "".join(sorted(s)) == "123456789":
            return s

    return ""


def attempt_1():
    max_pdp = ""
    for i in range(9, 10000):
        tmp = pandigital_product_maker(i)
        if tmp > max_pdp:
            max_pdp = tmp

    return max_pdp


def attempt_2():
    for i in range(9999, 9000, -1):
        tmp = pandigital_product_maker(i)
        if tmp != "":
            return tmp
    return None


def run():
    #return attempt_1()
    return attempt_2()


if __name__ == '__main__':
    print(run())
    #print(pandigital_product_maker(192))
    #print(pandigital_product_maker(9))
    #print(pandigital_product_maker(10))