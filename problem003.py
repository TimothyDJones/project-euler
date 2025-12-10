"""
Problem 3
https://projecteuler.net/problem=3

Largest Prime Factor
The prime factors of 13195 are 5,7,13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def main():
	TEST_VALUES = [13195, 600851475143]
	
	for v in TEST_VALUES:
		f = prime_factors(v)
		print("v: {v}, factors: {f}".format(v=v, f=f))


def prime_factors(n: int):
	i = 2
	factors = list()
	while i * i <= n:
		# If n is *NOT* divisible by i, increment i and continue.
		if n % i:
			i += 1
		# If n *IS* divisible by i, divide n by i and add i to list of factors.
		else:
			n //= i
			factors.append(i)
			
	if n > 1:
		factors.append(n)
		
	return factors

if __name__ == "__main__":
    main()
