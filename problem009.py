"""
Problem 9
https://projecteuler.net/problem=9

Special Pythagorean Triplet
A Pythagorean triplet is a set of three natural numbers, 𝑎 <𝑏 <𝑐, for which,
𝑎2+𝑏2=𝑐2.

For example, 32 +42 =9 +16 =25 =52.

There exists exactly one Pythagorean triplet for which 𝑎 +𝑏 +𝑐 =1000.
Find the product 𝑎⁢𝑏⁢𝑐.
"""

from math import sqrt

def main():
    MAX_VALUE = 1000
    prod = 0
    found = False
    
    for i in range(1, MAX_VALUE):
        for j in range(1, MAX_VALUE):
            code, c = check_pyth_triple(a=i, b=j)
            if code:
                # print(i, j, c)
                if (i + j + c) == 1000:
                    prod = (i * j * c)
                    found = True
                    break
                    
        if found:
            break
            
    print(prod)
    

def check_pyth_triple(a: int, b:int):
    c2 = a**2 + b**2
    c = sqrt(c2)
    if (int(c))**2 == c2:
        return True, int(c)
    else:
        return False, 0

if __name__ == "__main__":
    main()
