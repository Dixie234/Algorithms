from typing import List


def arrayManipulation(n:int, queries:List[List[int]]):
    result = 0
    arr = [0] * n
    for start, end, incr in queries:
        for i in range(start - 1, end):
            arr[i] += incr
            result = max(arr[i], result)
    return result