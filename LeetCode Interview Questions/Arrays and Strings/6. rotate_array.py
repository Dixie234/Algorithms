from collections import deque
from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    dq = deque(nums)
    dq.rotate(k)
    result = list(dq)
    for i, num in enumerate(result):
        nums[i] = num

nums = [1,2,3,4,5,6,7]

rotate(nums, 3)

print(nums)