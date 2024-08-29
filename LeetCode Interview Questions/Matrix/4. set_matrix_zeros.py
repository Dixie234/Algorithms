from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    column_updates = set()
    row_updates = set()
    columns = len(matrix)
    rows = len(matrix[0])
    for i in range(columns):
        for j in range(rows):
            if matrix[i][j] == 0:
                column_updates.add(j)
                row_updates.add(i)

    for column in column_updates:
        for i in range(columns):
            matrix[i][column] = 0

    for row in row_updates:
        for i in range(rows):
            matrix[row][i] = 0

#matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)

# row_updates = set()
# column_updates = set()
# for i, column in enumerate(matrix):
#     for j, row in enumerate(column):
#         if row == 0:
#             column_updates.add(i)
#             row_updates.add(j)

# for row in row_updates:
#     for i in range(len(matrix)):
#         matrix[row][i] = 0

# for column in column_updates:
#     for i in range(len(matrix)):
#         matrix[i][column] = 0

