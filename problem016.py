"""
Problem 16
https://projecteuler.net/problem=16

Power Digit Sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 16.

What is the sum of the digits of the number 2^1000?
"""

def main():
    POWER = 1000
    
    num = 2**POWER
    digit_sum = sum(list(map(int, list(str(num)))))

    print(digit_sum)


if __name__ == "__main__":
    main()
