def probs_31():

    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    ways_to_make_x = dict()
    for i in range(1, target+1):
        w = []
        for c in coins:
            y = i - c
            if y < 0:
                break

            if y == 0:
                w.append([c])
                break

            if y > 0:
                w_prev = ways_to_make_x[y]
                for wp in w_prev:
                    w.append(sorted([c] + list(wp)))

        w = tuple([tuple(l) for l in w])
        ways_to_make_x[i] = set(tuple(w))

    print(len(ways_to_make_x[target]))



def e28(n):
    spiral_sum = 1
    for i in range(3, n+2, 2):
        spiral_sum = 4*(i**2)-6*(i-1) + spiral_sum

    return spiral_sum

e28(5)
print(e28(1001))

5391546261
669171001