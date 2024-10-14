from typing import List


def add_edge(adj, i, j):
    adj[i].append(j) 
    adj[j].append(i)  # Undirected
    
def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if n == 1 and source == 0 and destination == 0:
        return True

    adj = { i:[] for i in range(n) }
    for edge in edges:
        add_edge(adj, edge[0], edge[1])
    
    return destination in adj[source]

n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
result = validPath(n, edges, 5, 9)
print(result)
    