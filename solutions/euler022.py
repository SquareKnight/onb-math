"""Names scores

#File
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import resources.resources as r


def namescore(name):
    score = 0
    for c in name:
        score += ord(c)-64
    return score


def namescore_2(name):
    score = 0
    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in name:
        score += alphabet.index(c)
    return score


def attempt_2():
    data = r.readfile("022.txt")
    names = sorted([[ord(c)-64 for c in n.replace('"', '')] for n in data.split(',')])
    total = 0
    for i in range(len(names)):
        total += (i+1) * sum(names[i])

    return total


def attempt_1():
    data = r.readfile("022.txt")
    names = sorted([n.replace('"', '') for n in data.split(',')])

    total = 0
    for i in range(len(names)):
        total += (i+1) * namescore(names[i])
        #total += (i+1) * namescore_2(names[i])

    return total


def run():
    return attempt_1()
    #return attempt_2()


if __name__ == '__main__':
    print(run())
    #print(namescore_2("COLIN"))