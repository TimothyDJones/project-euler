"""
Problem 36
https://projecteuler.net/problem=36

Double-base Palindromes
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from pprint import pprint


def main():
    palindromes = dict()

    for n in range(1, 1_000_000):
        if is_palindrome(n):
            binary = to_base(n, 2)
            if is_palindrome(binary):
                palindromes[n] = binary

    pprint(palindromes)
    print(sum(palindromes.keys()))


def is_palindrome(n: int|str):
    if isinstance(n, int):
        n = str(n)

    if n == n[::-1]:
        return True

    return False

def to_base(number: int, base: int):
    """
    Converts number to specified base.
    Returns result in string.
    """
    if not number or number < 0:
        return "0"

    digits = list()
    while number:
        digits.append(number % base)
        number //= base

    # print(digits)

    return "".join([str(i) for i in list(reversed(digits))])

if __name__ == "__main__":
    main()
