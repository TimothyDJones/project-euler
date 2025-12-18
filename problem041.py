"""
Problem 41
https://projecteuler.net/problem=41

Pandigital Prime
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
from itertools import permutations
from math import sqrt
from pprint import pprint


def main():
    max_pandigital_prime = 0

    for i in range(1, 10):
        digits = list(map(str, (range(1, i + 1))))
        s_n = "".join(digits)
        nums = [int(n) for n in ["".join(c) for c in permutations(s_n)]]
        # print(digits, s_n, nums)
        for m in nums:
            if is_prime(m):
                print(m)
                if m > max_pandigital_prime:
                    max_pandigital_prime = m


    print("\t", max_pandigital_prime)


def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    main()
