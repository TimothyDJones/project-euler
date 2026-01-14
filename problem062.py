"""
Problem 62
https://projecteuler.net/problem=62

Cubic Permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""
from math import sqrt
from pprint import pprint
import time


def main():
    MAX_VALUE = 10000
    cubes = {} # key = sorted list of digits of cube as string, value = list of original cubes
    min_cubes = list()

    for i in range(MAX_VALUE):
        c = i**3
        sorted_digits = "".join(sorted([d for d in str(c)]))
        if not cubes.get(sorted_digits):
            cubes[sorted_digits] = [c]
        else:
            cubes[sorted_digits].append(c)

    # Find *minimum* value among list of cubes with 5 values.
    for k, v in cubes.items():
        if len(v) == 5:
            min_cubes.append(min(v))

    # Get the minimum among all minimums with 5 values.
    print(min(min_cubes))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
