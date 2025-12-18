"""
Problem 39
https://projecteuler.net/problem=39

Integer Right Triangles
If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.

{20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p <= 1000, is the number of solutions maximised?
"""
from math import sqrt
from pprint import pprint


def main():
    max_solutions_count = 0
    p_max_solutions = 0

    solutions = find_solutions(1000)

    for k, v in solutions.items():
        print(k, v)
        if len(v) > max_solutions_count:
            max_solutions_count = len(v)
            p_max_solutions = k

    print("\t", p_max_solutions)

def is_right_triangle(a: int, b: int, c: int):
    if not (c > a and c > b):
        return False

    if not ((a**2 + b**2) == c**2):
        return False

    return True

def find_solutions(limit: int):
    solutions = dict()
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            for c in range(b, limit + 1):
                p = (a + b + c)
                if p > 1000:
                    continue
                if is_right_triangle(a, b, c):
                    print(a, b, c, p)
                    try:
                        solutions[p].append((a, b, c))
                    except Exception:
                        solutions[p] = list()
                        solutions[p].append((a, b, c))

    return solutions


if __name__ == "__main__":
    main()
