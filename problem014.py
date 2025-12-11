"""
Problem 14
https://projecteuler.net/problem=14

Longest Collatz Sequence


The following iterative sequence is defined for the set of positive integers:

    𝑛 →𝑛/2    (𝑛 is even)
    𝑛 →3⁢𝑛 +1  (𝑛 is odd)

Using the rule above and starting with 13, we generate the following sequence:
13→40→20→10→5→16→8→4→2→1.

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def main():
    MAX_NUMBER = 1_000_000
    max_seqn_length = 0
    max_start_num = 0
    
    for i in range(1, MAX_NUMBER):
        seqn = collatz_seqn(i)
        # print(seqn)
        if len(seqn) > max_seqn_length:
            max_seqn_length = len(seqn)
            max_start_num = i
            
    print(max_seqn_length, max_start_num)
    

def collatz_seqn(n: int):
    seqn = list()
    
    while n > 1:
        seqn.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = (3 * n + 1)
            
        if n == 1:
            seqn.append(n)
            break
            
    return seqn

if __name__ == "__main__":
    main()
