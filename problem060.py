"""
Problem 60
https://projecteuler.net/problem=60

Prime Pair Sets
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""
from math import sqrt
from pprint import pprint
import time


def main():
    MAX_PRIME = 10000
    sum_primes = 0
    primes = sieve_of_erosthenes(MAX_PRIME)

    for a in primes:
        for b in primes:
            if b < a: continue
            if is_prime_pair(a, b):
                for c in primes:
                    if c < b: continue
                    if (is_prime_pair(a, c)
                        and is_prime_pair(b, c)):
                        for d in primes:
                            if d < c: continue
                            if (is_prime_pair(a, d)
                                and is_prime_pair(b, d)
                                and is_prime_pair(c, d)):
                                for e in primes:
                                    if e < d: continue
                                    if (is_prime_pair(a, e)
                                        and is_prime_pair(b, e)
                                        and is_prime_pair(c, e)
                                        and is_prime_pair(d, e)):
                                        print(a, b, c, d, e)
                                        sum_primes = a + b + c + d + e
                                        print(sum_primes)
                                        return


def sieve_of_erosthenes(n: int):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [p for p in range(2, n + 1) if primes[p]]

def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True

def is_prime_pair(a: int, b: int):
    n = int(str(a) + str(b))
    m = int(str(b) + str(a))
    if is_prime(n) and is_prime(m):
        return True

    return False


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
