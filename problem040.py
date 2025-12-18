"""
Problem 40
https://projecteuler.net/problem=40

Champernowne's Constant
An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part, find the value of the following expression.
d(1) x d(10) x d(100) x d(1000) x d(10000) x d(100000) x d(1000000)

"""
from math import sqrt
from pprint import pprint


def main():
    s_n = ""
    prod = 1

    for n in range(1, 1_000_000):
        s_n += str(n)
        if len(s_n) > 1_000_000:
            break

    s = [int(i) for i in list(s_n)]

    for i in range(7):
        print(i, s[(10**i - 1)])
        prod *= s[(10**i - 1)]

    print("\t", prod)


if __name__ == "__main__":
    main()
