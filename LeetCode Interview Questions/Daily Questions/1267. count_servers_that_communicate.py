from collections import Counter, deque
from typing import List

#Correct solution: Count number of servers which are the only server on that row and column line
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

#Incorrect solution as this counts number of servers which are adjacent to one another. 
#Not just in the same row/col
def countServers(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    servers = [(i, j) for j in range(cols) for i in range(rows) if grid[i][j] == 1]
    if not servers:
        return 0
    
    visited = set()
    result = 0

    def bfs(root):
        queue = deque([root])
        connections = 1
        while queue:
            curr_row, curr_col = queue.popleft()
            visited.add((curr_row, curr_col))

            dimensions = [(curr_row + 1, curr_col), (curr_row, curr_col + 1), (curr_row - 1, curr_col), (curr_row, curr_col - 1)]
            for new_row, new_col in dimensions:
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or (new_row, new_col) in visited:
                    continue
                if grid[new_row, new_col] == 1:
                    queue.append((new_row, new_col))
                connections += grid[new_row][new_col]
                visited.add((new_row, new_col)) 
        return connections if connections > 1 else 0           

    for server in servers:
        if server not in visited:
            result += bfs(server)

    return result
        
