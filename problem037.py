"""
Problem 37
https://projecteuler.net/problem=37

Truncatable Primes
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from math import sqrt
from pprint import pprint


def main():
    truncatable_primes = list()

    for n in range(2, 1_000_000):
        if is_prime(n):
            s_n = str(n)
            t_prime = True
            for i in range(1, len(s_n)):
                # print(n, i, int(s_n[i:]), int(s_n[:-i]))
                if not is_prime(int(s_n[i:])):
                    t_prime = False
                    break
                if not is_prime(int(s_n[:-i])):
                    t_prime = False
                    break

            if t_prime and n > 9:
                print(n)
                truncatable_primes.append(n)

    print(truncatable_primes)
    print(sum(truncatable_primes))


def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()
