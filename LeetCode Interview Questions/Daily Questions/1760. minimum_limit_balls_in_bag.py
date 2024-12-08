from math import ceil
from typing import List

#max heap didn't work (greedy approach)
#binary search for minimum number which satifies the reduction of the maximum number in nums
#inside the range of operations set by max operations
def minimumSize(nums: List[int], maxOperations: int) -> int:
    def can_divide(max_balls):
        ops = 0
        for num in nums:
            ops += ceil(num / max_balls) -1
            if ops > maxOperations:
                return False
        return True
    
    #minimum search therefore use adjusted binary search
    l = 1
    h = max(nums)
    #using < instead of <= due to the inclusion of successful results 
    while l < h:
        m = (l + h) // 2
        #no 3rd if case as we're looking for the smallest valid value, not a specific value
        if can_divide(m):
            #just set to m as we want to include the successful case in our results
            h = m
        else:
            l = m + 1
    #return l as this stores the minimum number
    return l
            