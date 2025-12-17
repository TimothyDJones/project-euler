"""
Problem 32
https://projecteuler.net/problem=32

Pandigital Products
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from pprint import pprint


def main():
    DIGITS = list(range(1, 10))
    pandigital_products = set()

    for a in range(1, 2001):
        for b in range(1, 2001):
            # If any digits overlap between a and b, then it's not pandigital.
            if set(list(str(a))).intersection(set(list(str(b)))):
                continue
            prod = a * b
            l = sorted([int(i) for i in [*list(str(a)), *list(str(b)), *list(str(prod))]])
            if 0 in l or len(l) != 9 or l[0] != 1 or l[8] != 9:
                continue
            # print(a, b, prod, l)
            if l == DIGITS:
                print("\t", a, b, prod)
                pandigital_products.add(prod)


    print(pandigital_products)
    print(sum(pandigital_products))

if __name__ == "__main__":
    main()
