import copy
from itertools import combinations
from typing import List

def combine(n: int, k: int) -> List[List[int]]:
    result = []
    def backtrack(start, combo):

        if len(combo) == k:
            result.append(combo)
        else:
            for num in range(start, n + 1):
                temp = combo[:]
                temp.append(num)
                backtrack(num + 1, temp)
    backtrack(1, [])

    return result

#using python inbuild itertools function
def combine(n: int, k: int) -> List[List[int]]:
    return combinations(range(1, n + 1), k)

def combine_tooslow(n: int, k: int) -> List[List[int]]:
    result = set()
    def backtrack(num, combo):
        nonlocal result

        if len(combo) == k:
            result.add(tuple(combo))
        else:
            for i in range(num, n + 1):
                temp = copy.deepcopy(combo)
                temp.add(i)
                backtrack(num + 1, temp)
    backtrack(1, set())

    return result

n = 5
k = 3
result = combine(n, k)
print(result)