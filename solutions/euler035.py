"""Circular primes
limit;Test to number;int;1000000
#prime
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import solutions.libEuler as e

def attempt_1(limit):
    primes = [str(p) for p in e.primes_list(2, limit, False)]
    ret = [p for p in primes if len(p) == 1]

    for i in range(2, len(str(limit))):
        subset = [p for p in primes if len(p) == i and \
                  not any (c in ['0', '2', '4', '6', '8', '5'] for c in p)]

        while subset:
            s = subset[0]

            # Get the rotations as follows:
            #                                for g in range(i)                      A number of len 2 has 2 rotations, 3 digs=3 rots etc...
            #                                                                       So do the following n times where n is # digits
            #                  [(s+s)                                               Concatenate our object to itself
            #                        [g:g+i]                                        and take a substring of length n starting at positions 0-(n-1)
            #                                                                       This rotates because we have a number 1234 concatenated to 1234,
            #                                                                       and we take 4 substrings starting at pos 0, 1, 2, 3:
            #                                                                       1234, 2341, 3412, 4123
            #      [r for r in                                ] if r in subset]     And each element on the new list is only kept if it is in the prime subset itself.
            rots = [r for r in [(s+s)[g:g+i] for g in range(i)] if r in subset]

            if len(rots) == i:
                ret.extend(set(rots))

            for x in set(rots):
                subset.remove(x)

    return len(ret)


def run(limit):
    return attempt_1(limit)


if __name__ == '__main__':
    print(run(100))
    #print(run(10**6))
