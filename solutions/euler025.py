"""1000-digit Fibonacci number
n;Length of Fib number;int;1000
#Fibonacci
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def fibonacci(a=1, b=1):
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b


def attempt_2(n):
    fib_iter = fibonacci(0, 1)
    for i, f in enumerate(fib_iter):
        if len(str(f)) >= n:
            return i


def attempt_1(n):
    a, b, i = 1, 1, 2
    while len(str(b)) < n:
        a, b, i = b, a+b, i+1
    return i


def run(n):
    #return attempt_1(n)
    return attempt_2(n)

if __name__ == '__main__':
    #print(run(3))
    print(attempt_2(1000))