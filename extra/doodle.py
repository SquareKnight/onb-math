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

def get_next_digit(numer, denom):
    next_dig, modulo = divmod(numer, denom)
    yield (next_dig, modulo)
    while True:
        modulo *=10
        next_dig, modulo = divmod(modulo, denom)
        yield (next_dig, modulo)


for q in range(999, 980, -1):
    dig_iter = get_next_digit(1, q)
    mods_seen = []
    t = next(dig_iter)
    while t[1] not in mods_seen and t[1] != 0:
        mods_seen.append(t[1])
        # print(t[0])
        t = next(dig_iter)

    print(q, len(mods_seen), mods_seen)