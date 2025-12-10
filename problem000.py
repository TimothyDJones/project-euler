"""
Problem 0

A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 52 = 5 ×5 = 25; it is also an odd square.

The first 5 square numbers are: 1,4,9,16,25, and the sum of the odd squares is 1 +9 +25 =35.

Among the first 961 thousand square numbers, what is the sum of all the odd squares?
"""

def main():
	n = 0
	sum_odd_squares = 0

	while n < 961_000:
		n += 1
		sq = n * n
		if sq % 2:
			sum_odd_squares += sq
			
	print(sum_odd_squares)		


if __name__ == "__main__":
    main()
