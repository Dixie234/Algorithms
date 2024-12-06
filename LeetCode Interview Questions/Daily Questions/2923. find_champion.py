from typing import List


def findChampion(grid: List[List[int]]) -> int:
    new_grid = []
    for i in range(len(grid)):
        column = []
        for j in range(len(grid[0])):
            column.append(grid[j][i])
        new_grid.append(column)
    totals = [sum(row) for row in new_grid]
    return totals.index(0)

#using single pass of data and early stopping
def findChampion(grid: List[List[int]]) -> int:
    length = len(grid)
    for i in range(len(grid)):
        total = sum(grid[i])
        if total == (length - 1):
            return i
    return -1

grid = [[0, 0, 1], [1, 0, 1], [0, 0, 0]]
    
        
          
        