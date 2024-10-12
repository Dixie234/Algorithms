from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    if len(grid) == 1 and len(grid[0]) == 1:
        return grid[0][0]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                min_val = grid[i][j - 1]
            elif j == 0:
                min_val = grid[i - 1][j]
            else:
                min_val = min(grid[i][j - 1], grid[i - 1][j])
            grid[i][j] = grid[i][j] + min_val
    return grid[-1][-1]