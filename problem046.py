"""
Problem 46
https://projecteuler.net/problem=46

Goldbach's Other Conjecture
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2 x 1^2
15 = 7 + 2 x 2^2
21 = 3 + 2 x 3^2
25 = 7 + 2 x 3^2
27 = 19 + 2 x 2^2
33 = 31 + 2 x 1^1

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from math import sqrt
from pprint import pprint

def main():
    result = 0

    primes = sieve_of_erosthenes(10_000)

    for n in range(9, 10_000, 2):
        if n in primes:
            continue
        is_valid = False
        p_n = [i for i in primes if i < n]
        # pprint(n)
        for p in p_n:
            s = ((n - p) // 2)
            if is_square(s):
                is_valid = True
                break

        if not is_valid:
            result = n
            break

    print(result)

def is_square(n: int):
    if n < 0:
        raise ValueError("Square number must be positive.")

    s = round(sqrt(n))  # Round square root to integer
    return (s * s == n)

def sieve_of_erosthenes(n: int):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [p for p in range(2, n + 1) if primes[p]]


if __name__ == "__main__":
    main()
