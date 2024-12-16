from heapq import heapify, heappop, heappush
from typing import List


#using priority queue
#Time complexity O(n + klog(n)) - push and pop of heap is log(n), and happens k times, therefore is klog(n) time
#and heap creation is O(n) time
#Space complexity O(n) - storage of separate heap
def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    if multiplier == 1:
        return nums
    
    nums_heap = [(num, i) for i, num in enumerate(nums)]
    heapify(nums_heap)
    for i in range(k):
        val, index = heappop(nums_heap)
        nums[index] *= multiplier
        heappush(nums_heap, (nums[index], index))

    return nums

#brute force approach
#Time complexity O(n * k) - iterating through the list to find the minimum value for every k times
#Space complexity O(1) - only variables created inside loop
def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:
    if multiplier == 1:
        return nums
    
    for i in range(k):
        index = nums.index(min(nums))
        nums[index] *= multiplier
    return nums  
