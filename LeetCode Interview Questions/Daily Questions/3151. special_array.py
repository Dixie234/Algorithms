from typing import List


def isArraySpecial(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    
    for i in range(1, len(nums)):
        prev = nums[i - 1] % 2 == 0
        curr = nums[i] % 2 == 0
        if prev == curr:
            return False
        
    return True 
