from collections import Counter, deque
from typing import List

#Count number of servers which are the only server on that row and column line
#Minus that from the maximum amount of servers
#Time Complexity O(n) - O(4n) in worst cause for case where every cell in grid is a server, simplifies to O(n)
#Space Complexity O(k + m + n) - creates a list of k servers long, and dictionaries for n and m row and column lengths in worst case
def countServers(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    servers = [(i, j) for j in range(cols) for i in range(rows) if grid[i][j] == 1]
    if not servers:
        return 0
    count_rows = Counter([row for row, col in servers])
    count_cols = Counter([col for row, col in servers])
    result = len(servers)
    for row, col in servers:
        if count_rows[row] == 1 and count_cols[col] == 1:
            result -= 1
    return result
    
