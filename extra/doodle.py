import solutions.libEuler as e


def probs_31(target):
  coins = [1, 2, 5, 10, 20, 50, 100, 200]
  ways_to_make = {c: 1 for c in range(0, target+1)}

  for c in coins[1:]:
    for k in ways_to_make:
      ref_k = k - c
      if (ref_k) in ways_to_make:
        ways_to_make[k] += ways_to_make[ref_k]
      print(c, k, ways_to_make[k])

  return ways_to_make[target], len(ways_to_make)



def find_factor(lst):
    factor = 0
    for i in range(max(lst), 0, -1):
        if all([p%i==0 for p in lst]):
            factor = i
            return factor


print(probs_31(200))