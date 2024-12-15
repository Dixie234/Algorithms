from heapq import heapify, heappop, heappush, heapreplace
from typing import List

def findScore(nums: List[int]) -> int:
    length = len(nums)
    nums_heap = [(num, i) for i, num in enumerate(nums)]
    heapify(nums_heap)
    marked = set()
    score = 0

    while nums_heap:
        num, index = heappop(nums_heap)
        if index not in marked:
            score += num
            marked.add(index)
            if index > 0:
                marked.add(index - 1)
            if index < length - 1:
                marked.add(index + 1)

    return score


