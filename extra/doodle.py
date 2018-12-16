from math import factorial


def permutate(lst, index):
    """
    Returns the lexicographic permutation of lst's elements at index N
    :param lst:     The items to permutate
    :param index:   The index into the lexigraphic catalog
    :return:        A re-ordered list of all of lst's elements 
    """""
    if not lst:
        return []

    if len(lst) == 1:
        return  lst

    def inner_permutate(lst, index):
        # len(lst) gets the number of list elements; factorial over that tells us the number of ways we can arrange them.
        # The given index must fall within that range, modulo enforces that
        index = index % factorial(len(lst))
        slot =  int(index / factorial(len(lst)-1))
        if len(lst) == 2:
            return [lst[index]] + [lst[1-index]]
        else:
            #print('popping el {0}  off list {1}'.format(slot, lst))
            return [lst.pop(slot)] + inner_permutate(lst, index)

    lst = sorted(lst)
    return inner_permutate(lst, index)


LISTS = [[], ['a'], ['a', 'b', 'c', 'd']]
TESTS = [(0, LISTS[0])
        ,(5, LISTS[0])
        ,(0, LISTS[1])
        ,(5, LISTS[1])
        ,(0, LISTS[2])
        ,(5, LISTS[2])
        ,(6, LISTS[2])
        ,(23, LISTS[2])
        ,(24, LISTS[2])
        ,(25, LISTS[2])
        ,(222, LISTS[2])
        ]

for t in TESTS:
    print(t[1], t[0], permutate(t[1], t[0]))

for i in range(48):
    print(permutate('abcd', i))

print(permutate('0123456789', 10**6-1))