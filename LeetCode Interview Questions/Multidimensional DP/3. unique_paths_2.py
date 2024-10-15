#unique paths 1
from typing import List


def uniquePaths(m: int, n: int) -> int:
    mapping = { 
        (1, 1): 1, 
        (0, 0): 0,
        (0, 1): 0,
        (1, 0): 0
    }

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 0 or j == 0:
                mapping[(i, j)] = 0
            elif i == 1 or j == 1:
                mapping[(i, j)] = 1
            else:
                mapping[i, j] = mapping[(i - 1, j)] + mapping[(i, j - 1)]

    return mapping[(m, n)]

m = 3
n = 7
result = uniquePaths(m, n)
print(result)

#unique paths 2
def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
        return 0
    
    height = len(obstacleGrid)
    width = len(obstacleGrid[0])

    if height == width == 1:
        return 1

    grid = [[0] * width for _ in range(height)]
    grid[0][0] = 1

    for i in range(1, height):
        if obstacleGrid[i][0] == 0:
            grid[i][0] = grid[i - 1][0]

    for i in range(1, width):
        if obstacleGrid[0][i] == 0:
            grid[0][i] = grid[0][i - 1]
    
    for i in range(1, height):
        for j in range(1, width):
            if obstacleGrid[i][j] == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[-1][-1]

grid = [[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
result = uniquePathsWithObstacles(grid)
print(result)
            

