"""
Problem 20
https://projecteuler.net/problem=20

Factorial Digit Sum
n! means n x (n - 1) x (n - 2) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""


def main():
    NUM = 100

    digits = [int(d) for d in list(str(fact_recur(100)))]

    # print(digits)
    print(sum(digits))


def fact_recur(n: int):
    if n < 0:
        raise ValueError("Factorial of negative integers is undefined.")
    if n == 0 or n == 1:
        return 1

    return n * fact_recur(n - 1)


if __name__ == "__main__":
    main()
