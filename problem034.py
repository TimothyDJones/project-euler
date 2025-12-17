"""
Problem 34
https://projecteuler.net/problem=34

Digit Factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from pprint import pprint


def main():
    curious = list()

    for n in range(3, 1_000_000):
        if is_curious(n):
            curious.append(n)

    print(curious)
    print(sum(curious))


def fact_recur(n: int):
    if n < 0:
        raise ValueError("Factorial of negative integers is undefined.")
    if n == 0 or n == 1:
        return 1

    return n * fact_recur(n - 1)

def is_curious(n: int):
    digits = [int(i) for i in list(str(n))]
    sum_digits = 0

    for i in digits:
        sum_digits += fact_recur(i)

    if sum_digits == n:
        return True

    return False

if __name__ == "__main__":
    main()
