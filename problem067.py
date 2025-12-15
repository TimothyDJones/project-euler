"""
Problem 67
https://projecteuler.net/problem=67

Maximum Path Sum II
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

# Heuristic: Build up the maximum partial sum for each position (i, j)
# within the triangle on a row-by-row basis. Thus, once we reach the last
# row, the maximum partial sum for this row is the solution for the
# entire triangle.

def main():
    with open("0067_triangle.txt", "r") as f:
        raw_data = [line.strip() for line in f.readlines()]

    triangle = [list(map(int, row.split(" "))) 
		for row in raw_data
        if row not in [""] ]
    ## triangle = [list(map(int, row))) for row in triangle]
    print(triangle)

    if check_triangle:
        row_partial_sums = list()
        row_partial_sums.append(triangle[0])

        for r in range(1, len(triangle)):
            row_partial_sums.append(calc_row_partial_sums(
                previous_row_partial_sums=row_partial_sums[r - 1],
                row=triangle[r]))

        print(max(row_partial_sums[len(triangle) - 1]))


def check_triangle(triangle: list(list[int])):
    """
    Triangle is defined as list of lists with each row of one element
    longer than previous row and each element an integer.
    """
    for idx, row in enumerate(triangle):
        if not (idx + 1) == len(row):
            raise ValueError("Data does not represent triangle.")
        for elem in row:
            try:
                int(elem)
            except Exception:
                raise ValueError(f"{str(elem)} is not an integer.")

    return True

def calc_row_partial_sums(previous_row_partial_sums: list[int],
        row: list[int]):
    """
    Find partial sums for this row, from its values and the partial
    sums of the *PREVIOUS* row.
    """
    row_partial_sums = [0] * len(row)

    # Only *ONE* path leads to start and end elements of row.
    row_partial_sums[0] = previous_row_partial_sums[0] + row[0]
    row_partial_sums[len(row) - 1] = (previous_row_partial_sums[len(row) - 2]
        + row[len(row) - 1])

    for i in range(1, len(row) - 1):
        row_partial_sums[i] = max(previous_row_partial_sums[i - 1],
            previous_row_partial_sums[i]) + row[i]

    print(row_partial_sums)
    return row_partial_sums


if __name__ == "__main__":
    main()
