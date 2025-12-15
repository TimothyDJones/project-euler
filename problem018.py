"""
Problem 18
https://projecteuler.net/problem=18

Maximum Path Sum I
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

# Heuristic: Build up the maximum partial sum for each position (i, j)
# within the triangle on a row-by-row basis. Thus, once we reach the last
# row, the maximum partial sum for this row is the solution for the
# entire triangle.

def main():
    t = """
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """

    triangle = [list(map(int, row.split(" "))) for row in
        [line.strip() for line in t.splitlines()]
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
