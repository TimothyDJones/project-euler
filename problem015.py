"""
Problem 15
https://projecteuler.net/problem=15

Lattice Paths
Starting in the top left corner of a 2 ×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 ×20 grid?
"""
from math import factorial

def main():
    GRID_SIZE = 20

    print(int(comb(2*GRID_SIZE, GRID_SIZE)))


def perm(n: int, k: int):
    return (factorial(n)/factorial(n - k))

def comb(n: int, k: int):
    return (perm(n, k)/factorial(k))


if __name__ == "__main__":
    main()
