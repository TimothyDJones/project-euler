"""
Problem 27
https://projecteuler.net/problem=27

Quadratic Primes
Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from math import sqrt
from pprint import pprint
import sys


def main():
    max_consec_primes = 0
    coeffs = tuple()

    # get_consec_primes(1, 41)
    # get_consec_primes(-79, 1601)
    # return

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes = get_consec_primes(a, b)
            if len(primes) > max_consec_primes:
                print("\t", a, b, primes)
                max_consec_primes = len(primes)
                coeffs = a, b

    print((coeffs[0] * coeffs[1]))

def get_consec_primes(a: int, b: int):
    primes = dict()
    for n in range(1000):
        m = n**2 + (a * n) + (b)
        if is_prime(m):
            if n == 0:
                primes[n] = m
            elif (n - 1) in primes.keys():
                primes[n] = m
            else:
                break
        else:
            break

    # print(a, b, primes)
    return primes

def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True



if __name__ == "__main__":
    main()
