"""
Problem 35
https://projecteuler.net/problem=35

Circular Primes
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from math import sqrt
from pprint import pprint


def main():
    circular_primes = set()

    for n in range(2, 1_000_000):
        if n in circular_primes:
            continue
        if is_prime(n):
            p = list()
            s_n = str(n)
            for i in range(len(s_n)):
                p.append(int(s_n[i:] + s_n[:i]))

            c_prime = True
            for i in p:
                if i == n:
                    continue
                if not is_prime(i):
                    c_prime = False
                    break

            if c_prime:
                print(p)
                circular_primes.update(p)

    print(circular_primes)
    print(len(circular_primes))


def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    main()
