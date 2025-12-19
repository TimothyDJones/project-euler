"""
Problem 50
https://projecteuler.net/problem=50

Consecutive Prime Sum
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13.

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

# Heuristic: Take the list of primes less than 1 million. Work down
# from the end of the list, building a "sliding window" of subset of
# the primes. Check that the sum of the subset (consecutive primes) is
# less than the upper bound and is itself prime. If so, check if the
# length of this subset is greater than previous longest subset and, if
# so, set this one as the new longest sequence.

from math import sqrt
from pprint import pprint

def main():
    MAX_NUM = 1_000_000
    longest_seq = list()
    primes = list()
    sum_primes = 0

    _primes = sorted(sieve_of_erosthenes(MAX_NUM + 1))
    # We only need the list of primes up to the point that the *SUM*
    # of the *ENTIRE* list is less than 1 million.
    for p in _primes:
        sum_primes += p
        if sum_primes > MAX_NUM:
            break

        primes.append(p)

    l = len(primes)
    j = l

    # For j, we work down and, for i, we work up until we meet "near"
    # the middle of the list of primes.
    while j != 0:
        i = 0
        while i + j < l + 1:
            seq = primes[i:i + j]
            # print(len(seq), sum(seq))
            sum_seq = sum(seq)
            if sum_seq <= MAX_NUM:
                if is_prime(sum_seq):
                    # print(i, j, sum_seq, len(seq), seq)
                    if len(seq) > len(longest_seq):
                        longest_seq = seq

            i += 1
        j -= 1

    print(len(longest_seq), longest_seq)
    print(sum(longest_seq))


def is_prime(n: int):
    if n <= 1:
        return False

    for i in range(2, (int(sqrt(n)) + 1)):
        if n % i == 0:
            return False

    return True

def sieve_of_erosthenes(n: int):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [p for p in range(2, n + 1) if primes[p]]


if __name__ == "__main__":
    main()
