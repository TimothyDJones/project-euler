"""
Problem 28
https://projecteuler.net/problem=28

Number Spiral Diagonals
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from pprint import pprint


def main():
    SPIRAL_DIM = 1001
    # SPIRAL_DIM = 5
    DIRS = [
        [1, 0], # right
        [0, 1], # down
        [-1, 0], # left
        [0, -1] # up
    ]
    spiral = [[None for i in range(SPIRAL_DIM)] for j in range(SPIRAL_DIM)]
    sum_diagonals = 0

    # Build spiral
    # Start in middle row and column.
    row, col = SPIRAL_DIM // 2, SPIRAL_DIM // 2
    num = 1
    _dir = DIRS[3]

    while True:
        spiral[row][col] = num

        if ((row == col)
            or ((col + row) == (SPIRAL_DIM - 1))):
            # print(row, col, num)
            sum_diagonals += num

        if row == 0 and col == (SPIRAL_DIM - 1):    # Upper right corner
            break

        num += 1

        if _dir == DIRS[0]:
            if spiral[row + 1][col] == None:
                _dir = DIRS[1]
                row, col = row + 1, col
            else:
                row, col = row, col + 1
        elif _dir == DIRS[1]:
            if spiral[row][col - 1] == None:
                _dir = DIRS[2]
                row, col = row, col - 1
            else:
                row, col = row + 1, col
        elif _dir == DIRS[2]:
            if spiral[row - 1][col] == None:
                _dir = DIRS[3]
                row, col = row - 1, col
            else:
                row, col = row, col - 1
        elif _dir == DIRS[3]:
            if spiral[row][col + 1] == None:
                _dir = DIRS[0]
                row, col = row, col + 1
            else:
                row, col = row - 1, col

    # pprint(spiral)
    print(sum_diagonals)

if __name__ == "__main__":
    main()
