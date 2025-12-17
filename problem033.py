"""
Problem 33
https://projecteuler.net/problem=33

Digit Cancelling Fractions
The fraction 48/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from fractions import Fraction
from pprint import pprint


def main():
    curious = list()
    curious_prod = Fraction(1, 1)

    # Only consider fractions with 2-digit numerators and denominators.
    for n in range(10, 100):
        for d in range(n + 1, 100):
            if is_curious(n, d):
                print(n, d)
                curious.append(Fraction(n, d))  # Use Fraction class to reduce to lowest terms.

    for f in curious:
        curious_prod *= f

    print(curious, curious_prod)
    print(curious_prod.denominator)

def is_curious(n: int, d: int):
    f = Fraction(n, d)
    if f >= 1:
        return False

    n_digits = [int(i) for i in str(n)]
    d_digits = [int(i) for i in str(d)]

    # Assume that we can only cancel between left digit of numerator
    # and right digit of denominator.
    if n_digits[1] == d_digits[0]:
        try:
            if Fraction(n_digits[0], d_digits[1]) == f:
                return True
        except Exception:
            pass

    return False

if __name__ == "__main__":
    main()
