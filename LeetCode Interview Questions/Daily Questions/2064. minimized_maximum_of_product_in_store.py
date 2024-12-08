from math import ceil
from typing import List

#very similar to 1760. minimum_limit_balls_in_bag
def minimizedMaximum(n: int, quantities: List[int]) -> int:
    def can_divide(max_quant):
        stores = 0
        for quant in quantities:
            stores += ceil(quant / max_quant)
            if stores > n:
                return False
        return True
    
    l = 1
    h = max(quantities)
    while l < h:
        m = (l + h) // 2
        if can_divide(m):
            h = m
        else:
            l = m + 1
    return l