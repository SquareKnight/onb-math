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

def test(x):
    s = (num_as_word(x), num_as_word(x, ' '))
    print(s[1], len(s[0]))

som = 0
for q in range(1, 1000+1):
    som += len(num_as_word(q))
print(som)
