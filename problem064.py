"""
Problem 64
https://projecteuler.net/problem=64

Odd Period Square Roots

All square roots are periodic when written as continued fractions and can be written in the form:
√N = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + ...)))

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4; (1, 3, 1, 8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:
√2 = [1; (2)], period = 1
√3 = [1; (1, 2)], period = 2
√5 = [2; (4)], period = 1
√6 = [2; (2, 4)], period = 2
√7 = [2; (1, 1, 1, 4)], period = 4
√8 = [2; (1, 4)], period = 2
√10 = [3; (6)], period = 1
√11 = [3; (3, 6)], period = 2
√12 = [3; (2, 6)], period = 2
√13 = [3; (1, 1, 1, 1, 6)], period = 5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?

"""

# See https://charlesreid1.github.io/computing-square-roots-part-2-using-continued-fractions.html
# for heuristic to determine values of continued fraction.

from math import sqrt, pow
from pprint import pprint
import time


def main():
    MAX_VALUE = 10001
    # MAX_VALUE = 100
    count_odd_period = 0

    for n in range(2, MAX_VALUE):
        # If perfect square, skip number.
        ns = nearest_square(n)
        if n == ns:
            continue

        c_f = cont_frac2(n)
        if not (len(c_f[1:]) % 2 == 0):
            count_odd_period += 1

    print(count_odd_period)

def cont_frac2(n: int):
    m0, d0, a0 = 0, 1, int(sqrt(n))

    exp = [a0]
    m, d, a = m0, d0, a0

    while a != (2 * a0):
        m = d * a - m
        d = (n - m * m) // d
        a = int((a0 + m) / d)
        # print(n, m, d, a)
        exp.append(a)

    # print(exp)
    return exp


def nearest_square(n: int):
    i = int(pow(n, 0.5))
    return (i*i)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
