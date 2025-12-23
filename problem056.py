"""
Problem 56
https://projecteuler.net/problem=56

Powerful Digit Sum
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a,b < 100, what is the maximum digital sum?
"""
from itertools import groupby
from math import sqrt
from pprint import pprint


def main():
    max_sum_digits = 0

    for a in range(1, 100):
        for b in range(1, 100):
            x = a**b
            digit_sum = sum_digits(x)
            if digit_sum > max_sum_digits:
                max_sum_digits = digit_sum

    print(max_sum_digits)

def sum_digits(n: int):
    return sum(list(map(int, list(str(n)))))


if __name__ == "__main__":
    main()
