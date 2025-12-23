"""
Problem 57
https://projecteuler.net/problem=57

Square Root Convergents
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + (1 / 2 + (1 / 2 + (1 / 2 + ...

By expanding this for the first four iterations, we get:
1 + 1/2 = 3/2 = 1.5
1 + 1 / (2 + 1/2) = 7/5 = 1.4
1 + 1 / (2 + (1 / (2 + 1/2))) = 17/12 = 1.41666...
1 + 1 / (2 + (1 / (2 + 1/ (1 / (2 + 1/2))))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""
from fractions import Fraction
from math import sqrt
from pprint import pprint


def main():
    count_num_greater_den = 0

    fracs = [f for f in sqrt_two(1000)]
    # pprint(fracs)
    for f in fracs:
        if len(str(f.numerator)) > len(str(f.denominator)):
            count_num_greater_den += 1


    print(count_num_greater_den)


def sqrt_two(iterations):
    d = Fraction(1/2)
    for i in range(iterations):
        d = Fraction(1/(2 + d))
        yield 1 + d


if __name__ == "__main__":
    main()
