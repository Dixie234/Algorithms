from heapq import heapify, heappop, heappush, heappushpop
from math import floor, sqrt
from typing import List

def pickGifts(gifts: List[int], k: int) -> int:
    gifts_heap = [val * -1 for val in gifts]
    heapify(gifts_heap)
    max_val = heappop(gifts_heap)
    for i in range(k):
        sqrt_val = floor(sqrt(max_val * -1)) * -1
        max_val = heappushpop(gifts_heap, sqrt_val)
    heappush(gifts_heap, max_val)
    return sum([val for val in gifts_heap]) * -1
    