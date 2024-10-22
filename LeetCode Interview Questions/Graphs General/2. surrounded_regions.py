from collections import deque
from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    row_length, col_length = len(board), len(board[0])
    visited = set()

    def bfs(row, col):
        queue = deque([(row, col)])
        region = set([(row, col)])
        visited.add((row, col))
        touch_edge = False
        if row == 0 or row == (row_length - 1) or col == 0 or col == (col_length - 1):
            touch_edge = True

        while queue:
            row, col = queue.popleft()
            directions = [(row, col - 1), (row - 1, col), (row, col + 1), (row + 1, col)]
            for row_dir, col_dir in directions:
                if 0 <= row_dir < row_length and 0 <= col_dir < col_length and board[row_dir][col_dir] == "O" and (row_dir, col_dir) not in visited:
                    queue.append((row_dir, col_dir))
                    visited.add((row_dir, col_dir))
                    region.add((row_dir, col_dir))
                    if row_dir == 0 or row_dir == (row_length - 1) or col_dir == 0 or col_dir == (col_length - 1):
                        touch_edge = True

        if not touch_edge:
            for row, col in region:
                board[row][col] = "X"
    
    for row in range(row_length):
        for col in range(col_length):
            if (row, col) not in visited and board[row][col] == "O":
                bfs(row, col)



    
    
        