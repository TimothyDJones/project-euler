"""
Problem 10
https://projecteuler.net/problem=10

Summation of Primes
The sum of the primes below 10 is 2 +3 +5 +7 =17.

Find the sum of all the primes below two million.
"""

from math import sqrt

def main():
    MAX_PRIME = 2_000_000
    _max, m, idx = 0, 3, 0
    
    while _max < MAX_PRIME:
        p = sieve_of_erosthenes((10**m))
        _max = max(p)
        m += 1
        
    for i in range(MAX_PRIME):
        try:
            idx = p.index((MAX_PRIME + i))
            break
        except Exception:
            pass

    print(sum(p[:idx]))
    

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
