from collections import deque
from typing import List


def add_edge(adj, i, j):
    adj[i].append(j) 
    adj[j].append(i)  # Undirected
    
#dfs solution
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if n == 1 and source == 0 and destination == 0:
        return True

    adj = [[] for _ in range(n)]
    for edge in edges:
        add_edge(adj, edge[0], edge[1])

    visited = dfs(adj, source)
    
    return visited[destination]

def dfs_rec(adj, visited, source):
    visited[source] = True

    for i in adj[source]:
        if not visited[i]:
            dfs_rec(adj, visited, i)


def dfs(adj, source):
    visited = [False] * len(adj)
    dfs_rec(adj, visited, source)
    return visited

#bfs solution: more efficent as it checks local edges first before moving on
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if n == 1 and source == 0 and destination == 0:
        return True

    adj = [[] for _ in range(n)]
    for edge in edges:
        add_edge(adj, edge[0], edge[1])

    return bfs(adj, source, destination)

def bfs(adj, source, destination):
    visited = [False] * len(adj)
    queue = deque([source])
    visited[source] = True

    while queue:
        curr = queue.popleft()
        if curr == destination:
            return True
        for adj_vertex in adj[curr]:
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                queue.append(adj_vertex)
    return False

n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
result = validPath(n, edges, 5, 9)
print(result)
    