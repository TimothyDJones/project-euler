"""
Problem 23
https://projecteuler.net/problem=23

Non-Abundant Sums
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from math import sqrt
from pprint import pprint

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

def is_abundant(n: int):
    # print(n, divisors(n))
    return (n < sum(divisors(n)))

MAX_NUMBER = 28123
ABUNDANTS = [n for n in range(1, MAX_NUMBER) if is_abundant(n)]

def main():

    abundants = list()
    not_sum_of_abundants = list()
    sum_of_abundants = list()

    for n in range(1, MAX_NUMBER):
        # if not any([((n - a) in abundants) for a in abundants if a < n]):
        #     print("\t", n)
        #     not_sum_of_abundants.append(n)
        # It is known that all even numbers above 46 can be expressed
        # as sum of two abundant numbers.
        if n % 2 == 0 and n > 46:
            continue
        if not is_sum_of_abundants(n):
            not_sum_of_abundants.append(n)

    # pprint(abundants)
    # pprint(not_sum_of_abundants)
    print(sum(not_sum_of_abundants))

def is_sum_of_abundants(n: int):
    for i in range(1, n + 1):
        if (ABUNDANTS.count(i)
            and ABUNDANTS.count(n - i)):
            print(n, i, n - i)
            return True

    return False


if __name__ == "__main__":
    main()
