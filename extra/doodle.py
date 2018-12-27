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

def fibonacci(a=1, b=1):
    yield a
    yield b
    while 1:
        a, b = b, a+b
        yield b

def probs_25():
    for i, q in enumerate(fibonacci(0, 1)):
        print(len(str(q)))
        if len(str(q))>=1000:
            return i

print(probs_25())