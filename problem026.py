"""
Problem 26
https://projecteuler.net/problem=26

Reciprocal Cycles
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

# Heuristic: Repeatedly perform "long division" on denominator. If there
# is no remainder, then we are done, because that means there is no
# cycle. If there is remainder, then we add it to a list of remainders.
# If the remainder is *ALREADY* in the list of remainders, that means
# we have the beginning of a cycle and can stop and add up the length
# of the remainders to determine the length the cycle.

from itertools import permutations
from pprint import pprint
import sys


def main():
    cycles = dict()

    # print(get_cycle_length_by_long_division(57))
    # return

    for d in range(1, 1000):
        cycles[d] = get_cycle_length_by_long_division(d)

    cycles = sorted(cycles.items(), key=lambda k: k[1])

    print(cycles[-1][0])


def get_cycle_length_by_long_division(denominator: int):
    digits = list()
    remainders = list()
    curr_num = 10

    while True:
        digit = curr_num // denominator
        curr_num = curr_num % denominator
        # print(curr_num, digits, remainders)
        if curr_num in remainders:
            break

        digits.append(digit)
        remainders.append(curr_num)

        curr_num *= 10
        if curr_num == 0:
            return 0        # No cycle

        while curr_num < denominator:
            curr_num *= 10
            digits.append(0)

    while remainders[0] != curr_num:
        remainders.pop(0)

    return len(remainders)


if __name__ == "__main__":
    main()
