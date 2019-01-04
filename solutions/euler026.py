"""Reciprocal cycles
n;Highest testcase;int;1000
#Division #reciprocal
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	    = 	0.5
1/3	    = 	0.(3)
1/4	    = 	0.25
1/5	    = 	0.2
1/6	    = 	0.1(6)
1/7	    = 	0.(142857)
1/8	    = 	0.125
1/9	    = 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def get_next_digit(numer, denom):
    digit, modulo = divmod(numer, denom)
    yield (digit, modulo)
    while True:
        modulo *= 10
        digit, modulo = divmod(modulo, denom)
        yield (digit, modulo)


def attempt_1(n):
    max_cycle_len = 0
    for q in range(n, 0, -1):
        dig_iter = get_next_digit(1, q)
        mods_seen = []
        while True:
            t = next(dig_iter)
            if t[1] == 0 or t[1] in mods_seen:
                break
            mods_seen.append(t[1])

        if len(mods_seen) > max_cycle_len:
            max_cycle_len = len(mods_seen)
            if len(mods_seen) == (q-1):
                return q, max_cycle_len

    return  max_cycle_len


def run(n):
    return attempt_1(n)


if __name__ == '__main__':
    print(run(10))