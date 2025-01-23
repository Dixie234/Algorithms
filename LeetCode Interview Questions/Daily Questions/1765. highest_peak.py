from collections import deque
from typing import List


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    rows, cols = len(isWater), len(isWater[0])
    result = [[-1 for j in range(cols)] for i in range(rows)]
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if isWater[i][j] == 1:
                result[i][j] = 0
                queue.append((i, j))
    while queue:
        row, col = queue.popleft()
        dimensions = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
        for new_row, new_col in dimensions:
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or result[new_row][new_col] != -1:
                continue
            queue.append((new_row, new_col))
            result[new_row][new_col] = result[row][col] + 1
    return result

isWater = [[0,0,1],[1,0,0],[0,0,0]]
result = highestPeak(isWater)
print(result)