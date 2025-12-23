"""
Problem 53
https://projecteuler.net/problem=53

Combinatoric Selections
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n!/r!(n - r)!, where r <= n, n! = n x (n - 1) x ... x 3 x 2 x 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than one-million?
"""

from math import sqrt
from pprint import pprint

def main():
    MIN_NUM = 1_000_000
    count = 0

    for n in range(1, 101):
        for r in range(1, n):
            if combinations(n, r) > MIN_NUM:
                count += 1

    print(count)


def memoize(f):
    cache = {}
    def _cache(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return _cache

@memoize
def fact_recur(n: int):
    if n < 0:
        raise ValueError("Factorial of negative integers is undefined.")
    if n == 0 or n == 1:
        return 1

    return n * fact_recur(n - 1)

def combinations(n: int, r: int):
    return (fact_recur(n)/(fact_recur(r)*fact_recur(n - r)))


if __name__ == "__main__":
    main()
