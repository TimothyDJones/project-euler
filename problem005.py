"""
Problem 5
https://projecteuler.net/problem=5

Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def main():
    MAX_VALUE = 1_000_000_000
    n = 2520
    
    divisble = False
    while n < MAX_VALUE and divisble == False:
        divisble = True
        n += 1
        for i in range(11, 21):
            if n % i:
                divisble = False
                break
                
    print(n)

if __name__ == "__main__":
    main()
