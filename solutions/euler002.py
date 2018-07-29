def attempt_1(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return [i for i in fib if i%2==0]
