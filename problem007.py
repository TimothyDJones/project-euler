"""
Problem 7
https://projecteuler.net/problem=7

10 001st Prime
By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def main():
    MAX_PRIME = 10001
    l, m = 0, 3
    
    while l < MAX_PRIME:
        p = sieve_of_erosthenes((10**m))
        l = len(p)
        m += 1

    print(p[10000])
    

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
