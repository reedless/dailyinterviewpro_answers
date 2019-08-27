'''
You are given a 2D array of integers.
Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
'''

def matrix_spiral_print(M):
    first_row = 0
    last_row = len(M) - 1

    first_column = 0
    last_column = len(M[0]) - 1

    res = []

    while (last_row > first_row and last_column > first_column):
        for i in range(first_column, last_column+1):
            res.append(M[first_row][i])
        for i in range(first_row+1, last_row):
            res.append(M[i][last_column])
        for i in range(last_column, first_column-1, -1):
            res.append(M[last_row][i])
        for i in range(last_row-1, first_row, -1):
            res.append(M[i][first_column])

        first_row += 1
        last_row -= 1
        first_column += 1
        last_column -= 1

    print(res)

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
