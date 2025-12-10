"""
Problem 1
https://projecteuler.net/problem=1

Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
	MAX_VALUE = 1000
	_sum = 0
	
	for n in range(MAX_VALUE):
		if n % 3 == 0 or n % 5 == 0:
			_sum += n
			
	print(_sum)
		

if __name__ == "__main__":
    main()
