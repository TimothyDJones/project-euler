"""
Problem 63
https://projecteuler.net/problem=63

Powerful Digit Counts

The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""
from math import sqrt
from pprint import pprint
import time


def main():
    MAX_VALUE = 100
    MAX_EXP = 100
    count_same_length_power = 0

    for n in range(1, MAX_VALUE):
        for exp in range(1, MAX_EXP):
            v = n**exp
            if len(str(v)) == exp:
                count_same_length_power += 1

    print(count_same_length_power)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
