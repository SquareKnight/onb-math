import solutions.libEuler as e

n = 28123
abundants = []
for i in range(1, n+1):
    d = e.divisors(i)
    if sum(d) > i:
        abundants.append(i)

print(abundants)

can_be_sums = []
for i in range(len(abundants)-1):
    for j in range(i, len(abundants)):
        q = abundants[i] + abundants[j]
        if q > n: break
        can_be_sums.append(q)

can_be_sums = set(can_be_sums)
print(can_be_sums)
print(sum([x for x in range(n) if x not in can_be_sums]))

exit()
# can n be written as the sum of two abundants?
# one way of testing that is n-(a) and checking if that is on the list
result = []
for i in range(1, n+1):
    valid = True
    for a in abundants:
        q = i-a
        if q <= 0:
            break
        else:
            if q in abundants:
                valid = False
                break
    print(i)
    if valid: result.append(i)

print(result)