"""
Problem 43
https://projecteuler.net/problem=43

Sub-string Divisibility
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d(1) be the 1st digit, d(2) be the 2nd digit, and so on. In this way, we note the following:

d(2)d(3)d(4) = 406 is divisible by 2
d(3)d(4)d(5) = 063 is divisible by 3
d(4)d(5)d(6) = 635 is divisible by 5
d(5)d(6)d(7) = 357 is divisible by 7
d(6)d(7)d(8) = 572 is divisible by 11
d(7)d(8)d(9) = 728 is divisible by 13
d(8)d(9)d(10) = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations
from pprint import pprint

def main():
    DIGIT_INDEX_PRIME_MAP = {
        2: 2,
        3: 3,
        4: 5,
        5: 7,
        6: 11,
        7: 13,
        8: 17
    }
    valid_nums = list()

    # nums = [1406357289]
    for d in permutations(range(10)):
        for k, v in DIGIT_INDEX_PRIME_MAP.items():
            n = (100 * d[k - 1] + 10 * d[k] + d[k + 1])
            if not n % v == 0:
                break
        else:
            # print(d)
            valid_nums.append(int("".join([str(i) for i in list(d)])))

    print(valid_nums)
    print(sum(valid_nums))


if __name__ == "__main__":
    main()
