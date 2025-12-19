"""
Problem 47
https://projecteuler.net/problem=47

Distinct Primes Factors
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
from math import sqrt
from pprint import pprint

def main():
    NUM_FACTORS = 4
    target = 0

    for n in range(1_000_000):
        distinct = True
        factors = set()
        for i in range(NUM_FACTORS):
            # print(n + i, is_prime(n + 1))
            if is_prime(n + i):
                distinct = False
                break
            f = set(prime_factors(n + i))
            # print(f)
            if not len(f) == NUM_FACTORS:
                distinct = False
                break

            factors = factors.union(f)

        if distinct:
            print(factors)
            target = n
            break

    print(target)


def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True

def prime_factors(n: int):
    i = 2
    factors = list()
    while i * i <= n:
        # If n is *NOT* divisible by i, increment i and continue.
        if n % i:
            i += 1
        # If n *IS* divisible by i, divide n by i and add i to list of factors.
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors


if __name__ == "__main__":
    main()
