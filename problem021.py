"""
Problem 21
https://projecteuler.net/problem=21

Amicable Numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into
n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71, and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import sqrt

def main():
    MAX_NUM = 10000
    amicable = set()

    d = {}

    for n in range(1, MAX_NUM):
        d[n] = sum(divisors(n))

    # print(d)

    for n, d_n in d.items():
        if d_n in d.keys():
            if d[d_n] == n and d_n != n:
                amicable.add(d_n)
                amicable.add(n)
    print(amicable)
    print(sum(list(amicable)))


def divisors(n: int):
    """
    Find *ALL* proper divisors of integer n.
    """
    d = list()
    ceil = int(sqrt(n)) + 1

    for i in range(1, ceil):
        if n % i == 0:
            d.append(i)

            if i != n // i:
                d.append(n // i)
    if n > 1:
        del d[1]

    return d


if __name__ == "__main__":
    main()
