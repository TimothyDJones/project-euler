"""
Problem 52
https://projecteuler.net/problem=52

Consecutive Prime Sum
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from math import sqrt
from pprint import pprint

def main():
    MAX_NUM = 1_000_000
    result = 0

    for x in range(1, MAX_NUM):
        valid = True
        for i in range(2, 7):
            # print(x, i * x)
            if not (len(set(list(str(x))).symmetric_difference(
                set(list(str(i * x))))) == 0):
                valid = False
                break

        if valid:
            result = x
            break
        else:
            continue


    print(result)


if __name__ == "__main__":
    main()
