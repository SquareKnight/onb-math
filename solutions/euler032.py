"""Pandigital products

#Multiplication #Pandigital
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

def attempt_1():
    pandigits = '123456789'
    result = []

    # set up aa loop for our number A, starting with determining its order of magnitude
    # we can stop at 4, because 1111 x 1 = 1111 (which totals 9 digits)
    # Therefore, there's no base number of 5 digits that, when multiplied with a 6th digit,
    # and combined with its product wil be under 10 digits long.
    for oom_a in range(1, 5):
        # NOTE that we'll only be multiplying small a's with larger b's, so this limit could be a lot lower that OoM 4,
        # but the code below takes care of that.

        # Now for number b:
        # The answer of the multiplication should be in the order of magnitude 9 - (len(a) + len(b))
        # Multiplying two numbers will always adhere to the rule:
        #       Length of a*b is always len(a) + len(b) - (0 or 1)
        # So, knowing the order of magnitude on A and setting a proxy oom for B, we can guess if those add up:
        possible_oombs = []
        for oomb_prox in range(oom_a, 10-oom_a):
            if 2 * (oom_a + oomb_prox) - 1 <= 9:
                possible_oombs.append(oomb_prox)

        # Get all the numbers of length oom_a
        for a in range(10**(oom_a-1), 10**oom_a):
            # and B
            for oom_b in possible_oombs:
                for b in range(10**(oom_b-1), 10**oom_b):
                    # get our pandigits candidate:
                    pdc = ''.join(sorted("{}{}{}".format(a, b, a*b)))
                    if len(pdc) > 9:    # a*b result is too big, we're done here
                        break

                    if pdc != pandigits:    # a*b result is too big, we're done here
                        continue

                    result.append(a*b)
    print(result)
    return sum(set(result))


def run():
    return attempt_1()


if __name__ == '__main__':
    print(run())