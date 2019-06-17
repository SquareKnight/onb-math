"""Pandigital multiples
limit;Perimiter up to n;int;1000
#triangle
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def attempt_1(limit):
    current_max = (0, [])
    for per in range(12, limit+1):
        valid_triplets = []
        for a in range(3, per):
            for b in range(a, per):
                c = per - (a+b)
                if c < b:
                    break
                if a**2 + b**2 == c**2:
                    valid_triplets.append((a, b, c))

        if len(valid_triplets) > len(current_max[1]):
            current_max = (per, valid_triplets)

    print(current_max)
    return current_max[0]


def attempt_2(limit):
    current_max = (0, [])

    generated_trips = []
    total_trips = []
    m, n = 2, 1
    while True:
        a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
        m = m + 1
        if a + b + c > limit:
            if len(generated_trips) == 0:
                break
            else:
                total_trips.extend(generated_trips)
                generated_trips = []
            n += 1
            m = n+1
        else:
            generated_trips.append((a, b, c))

    dict_perim = dict()
    for trip in total_trips:
        factor= 1
        new_trip  = tuple(t * factor for t in trip)
        s = sum(new_trip)
        while s <= limit:
            if s in dict_perim:
                dict_perim[s].append(new_trip)
            else:
                dict_perim[s] = [new_trip]

            factor += 1
            new_trip = tuple(t * factor for t in trip)
            s = sum(new_trip)

    for d in dict_perim:
        dict_perim[d] = set(dict_perim[d])
        if len(dict_perim[d]) > len(current_max[1]):
            current_max = (d, dict_perim[d])

    print(current_max)
    return current_max[0]

def run(limit):
    #return attempt_1(limit)
    return attempt_2(limit)


if __name__ == '__main__':
    print(run(1000))
