"""
Problem 6
https://projecteuler.net/problem=6

Sum Square Difference
The sum of the squares of the first ten natural numbers is,
12+22+...+102=385.

The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 −385 =2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def main():
    MAX_VALUE = 100
    
    sum_of_squares = sum([n * n for n in range(1, (MAX_VALUE + 1))])
    square_of_sums = (sum([n for n in range(1, (MAX_VALUE + 1))]))**2
                
    print((square_of_sums - sum_of_squares))

if __name__ == "__main__":
    main()
