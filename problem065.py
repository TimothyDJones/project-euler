"""
Problem 65
https://projecteuler.net/problem=65

Convergents of e

The square root of 2 can be written as an infinite continued fraction.
√2 = 1 + (1 / (2 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))))

The infinite continued fraction can be written, √2 = [1; (2)], (2) indicates that 2 repeats ad infinitum. In a similar way, √23 = [4; (1, 3, 1, 8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for √2.
1 + 1/2 = 3/2
1 + 1 / (2 + 1/2) = 7/5
1 + 1 / (2 + 1 / (2 + 1/2)) = 17/12
1 + 1 / (2 + 1 / (2 + 1 / (2 + 1/2))) = 41/29

Hence the sequence of the first ten convergents for √2 are:
1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,
e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]

The first ten terms in the sequence of convergents for e are:
2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

"""

# See https://charlesreid1.github.io/computing-square-roots-part-2-using-continued-fractions.html
# for heuristic to determine values of continued fraction.

from itertools import islice
from math import sqrt, pow
from pprint import pprint
import time


def main():
    sum_100_num_digits = 0

    e = list(islice(e_gen(), 100))
    pprint(e)
    numerator = rationalize(e)[0]
    sum_100_num_digits = sum([int(d) for d in str(numerator)])

    print(sum_100_num_digits)

def e_gen():
    yield 2
    k = 1
    while True:
        yield 1
        yield 2*k
        yield 1
        k += 1

def rationalize(fraction: list):
    if len(fraction) == 0:
        return (1, 0)
    elif len(fraction) == 1:
        return (fraction[0], 1)
    else:
        remainder = fraction[1:len(fraction)]
        (num, denom) = rationalize(remainder)
        return (fraction[0] * num + denom, num)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
