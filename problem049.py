"""
Problem 49
https://projecteuler.net/problem=49

Prime Permutations
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 4-digit number do you form by concatenating the three terms in this sequence?
"""
from itertools import permutations
from math import sqrt
from pprint import pprint

def main():
    delta = 3330
    MAX_NUM = 10000
    invalid_num = 1487
    result = ""

    for a in range(1000, MAX_NUM):
        if not is_prime(a) or a == invalid_num:
            continue

        b, c = a + delta, a + 2 * delta

        candidates = [int("".join(p)) for p in permutations(str(a))]

        if b in candidates and c in candidates:
            if ((not is_prime(b)) or (not is_prime(c))):
                continue

            result = str(a) + str(b) + str(c)
            break

    print(result)


def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()
