from typing import List


def findChampion(n: int, edges: List[List[int]]) -> int:
    in_count = {pair[1] for pair in edges}

    champion = None
    for i in range(n):
        if i not in in_count:
            if champion is not None:
                return -1
            else:
                champion = i
    return champion

n = 4
edges = [[0,2],[1,3],[1,2]]

        



