"""Power digit sum
e;Exponent;int;1000
#Basic
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


def run(e):
    return sum(list(map(int, str(2**e))))


if __name__ == '__main__':
    print(run(1000))