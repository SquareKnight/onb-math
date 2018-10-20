"""Longest Collatz sequence
n;Check up to n;int;1000000
#Collatz
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def attempt_1(n):
    longest_path = 0
    nr_for_lp = 0

    for i in range(1, n):
        j = i
        steps = 1
        while j > 1:
            steps += 1
            if j % 2 == 0:
                j = j / 2
            else:
                j = j * 3 + 1

        if steps > longest_path:
            longest_path = steps
            nr_for_lp = i

    return nr_for_lp


store = {1: 1}

def collatz(n):
    if n not in store:
        if n % 2 == 0:
            store[n] = collatz(n / 2) + 1
        else:
            store[n] = collatz(n * 3 + 1) + 1

    return store[n]

def attempt_2(n):
    ml = 0
    nr_for_ml = 0
    for i in range(1, n):
        length = collatz(i)
        if length > ml:
            ml = length
            nr_for_ml = i

    print(ml)
    return nr_for_ml



def run(n):
    #return attempt_1(n)
    return attempt_2(n)


if __name__ == '__main__':
    print(run(1000000))
