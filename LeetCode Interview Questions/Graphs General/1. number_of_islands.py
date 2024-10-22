from collections import deque
from typing import List

#when you find a land, do a bfs search of all it's connected lands and store them in visited
#when you come across another land, you therefore know it's a new island and repeat the process
def numIslands(grid: List[List[str]]) -> int:
    result = 0
    row_length, col_length = len(grid), len(grid[0])
    visited = set()

    def bfs(row, col):
        queue = deque([(row, col)])
        visited.add((row, col))

        while queue:
            row, col = queue.popleft()
            directions = [(row, col -1), (row - 1, col), (row, col + 1), (row + 1, col)]
            for row_dir, col_dir in directions:
                if 0 <= row_dir < row_length and 0 <= col_dir < col_length and grid[row_dir][col_dir] == "1" and (row_dir, col_dir) not in visited:
                    queue.append((row_dir, col_dir))
                    visited.add((row_dir, col_dir))

    for row in range(row_length):
        for col in range(col_length):
            if grid[row][col] == "1" and (row, col) not in visited:
                result += 1
                bfs(row, col)

    return result
