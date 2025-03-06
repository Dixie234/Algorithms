from typing import Counter, List


def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    counter_grid = Counter([i for row in grid for i in row])
    a = 0
    b = 0
    for i in range(1, (len(grid) ** 2) + 1):
        if i in counter_grid and counter_grid[i] == 2:
            a = i
        elif i not in counter_grid:
            b = i
        if a != 0 and b != 0:
            break
    return (a, b)

l = [[1,2,3],[4,5,6]]
print([i for row in l for i in row])