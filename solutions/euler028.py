"""Number spiral diagonals
n;Sidelength;int;1001
#spiral #square
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def attempt_1(n):
    spiral_sum = 1
    for i in range(n, 1, -2):
        for j in range(0, 4):
            spiral_sum += i**2 - (j*(i-1))
    return spiral_sum


def sums_of_corners(i):
    return 4*(i**2) - 6*(i-1)

def attempt_2(n):
    spiral_sum = 1
    for i in range(3, n+1, 2):
        spiral_sum += sums_of_corners(i)
    return spiral_sum

def run(n):
    return attempt_2(n)


if __name__ == '__main__':
    print(attempt_2(5))