"""Number letter counts
n;Numbers up to n;int;1000
#Basic
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""


def number_to_wordlist(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        , 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    other_magns = ['hundred', 'thousand']

    all_text = [[], ones, tens]
    all_text.extend(other_magns)

    ret = []
    new_n = 0
    if n < 20:
        ret.append(ones[n])
    else:
        s = str(n)
        x = int(s[0])
        magn = len(s)
        new_n = n - (x*10**(magn-1))

        if magn > 2:
            ret.extend([ones[x], all_text[magn]])
        elif magn == 2:
            ret.append(all_text[magn][x])

    if new_n > 0:
        if magn == 3:
            ret.append('and')
        ret.extend(number_to_wordlist(new_n))

    return ret


def num_as_word(n, delim = ''):
    s = number_to_wordlist(n)
    return delim.join(s)


def attempt_1(n):
    results = []
    for i in range(1, n+1):
        results.append(num_as_word(i))

    s = []
    for r in results:
        s.append(len(r))
    return sum(s)


def run(n):
    return attempt_1(n)


if __name__ == '__main__':
    print(run(5))
