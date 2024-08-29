import copy
from typing import List


def rotate(matrix: List[List[int]]) -> None:
    rev_matrix = copy.deepcopy(matrix[::-1])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = rev_matrix[j][i]
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = rotate(matrix)
print(result)