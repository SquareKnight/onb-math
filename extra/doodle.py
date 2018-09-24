import time

def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]


def tim(x):
    mx = 0
    def even_or_odd(n):

        if n % 2 == 0:
            return  n/2
        if n % 2 != 0:
            return (3 * n )+1

    check_list = []
    largest_list = []

    for n in range(2, x):
        list = []
        range_count = n
        while n != 1:
            test = even_or_odd(n)
            n = test
            list.append(n)
        check_list = list

        if len(check_list) >= len(largest_list):
            largest_list = check_list
            mx = range_count
            #print(len(largest_list),range_count)

            #print(n)
            #print(largest_list)
    return mx

def pim(x):
    dchains = {1: 0}
    for i in range(2, x+1):
        j = i
        chain_length = 0
        while j != 1:
            chain_length += 1
            if j % 2 == 0:
                j /= 2
            else:
                j = j * 3 + 1
            if j in dchains:
                chain_length += dchains[j]
                break

        dchains[i] = chain_length

    return keywithmaxval(dchains)


def pim2(x):
    dchains = {1: 0}
    for i in range(2, x+1):
        j = i
        chain = []
        chain_length = 0
        while j != 1:
            chain.append(j)
            if j % 2 == 0:
                j /= 2
            else:
                j = j * 3 + 1
            if j in dchains:
                chain_length += dchains[j]
                break
        chain_length += len(chain)

        q = chain.pop(0)
        while q not in dchains:
            dchains[q] = chain_length
            #print("Added {0}: {1}".format(q, chain_length))
            chain_length -= 1
            if len(chain) < 1:
                break
            q = chain.pop(0)


    return keywithmaxval(dchains)


import solutions.libEuler as e

if __name__ == "__main__":
    """
    x = 1*10**6
    start_time = time.time()
    #print(tim(x))
    end_time = time.time()
    print("total time:", (end_time - start_time))

    start_time = time.time()
    print(pim(x))
    end_time = time.time()
    print("total time:", (end_time - start_time))

    start_time = time.time()
    print(pim2(x))
    end_time = time.time()
    print("total time:", (end_time - start_time))
    """

    p = e.primes_list(1, 16)
    print(p)
    p = e.primes_list(1, 16, True)
    print(p)
