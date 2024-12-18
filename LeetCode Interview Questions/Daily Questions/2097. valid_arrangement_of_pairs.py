from collections import defaultdict, deque
from typing import List

def get_node_degrees(graph:List[List[int]]) -> tuple[defaultdict, defaultdict, deque]:
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    adjacency_matrix = defaultdict(deque)

    for start, end in graph:
        adjacency_matrix[start].append(end)
        in_degree[end] += 1
        out_degree[start] += 1

    return in_degree, out_degree, adjacency_matrix

def find_start_node(graph:List[List[int]]):
    inarr, outarr, adj_matrix = get_node_degrees(graph)
    start = 0
    for k, v in outarr.items():
        diff = v - inarr.get(k, 0)
        if diff == 1:
            return k, adj_matrix
        elif v > 0:
            start = k
    return start, adj_matrix

#Use heirolozers algorithm 
def validArrangement(pairs: List[List[int]]) -> List[List[int]]:        
    start, adj_matrix = find_start_node(pairs)
    path = deque()
    
    def postorder_dfs(node):
        while adj_matrix[node]:
            next = adj_matrix[node].popleft()
            postorder_dfs(next)
        path.appendleft(node)
    
    postorder_dfs(start)

    result = [[path[i - 1], path[i]] for i in range(1, len(path))]
    return result