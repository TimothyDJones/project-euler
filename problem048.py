"""
Problem 48
https://projecteuler.net/problem=48

Self Powers
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
from math import sqrt
from pprint import pprint

def main():
    MAX_NUM = 1000
    total = 0

    for n in range(1, MAX_NUM + 1):
        total += n**n

    print(str(total)[-10:])


if __name__ == "__main__":
    main()
