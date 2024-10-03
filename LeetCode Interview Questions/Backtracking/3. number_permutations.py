from itertools import permutations
from typing import List

#using python inbuild itertools function
def permute(nums: List[int]) -> List[List[int]]:
    return permutations(nums)

def permute(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []
    
    result = []
    length = len(nums)
    def backtrack(idx, combo):
        if idx == (length - 1):
            result.append(combo[:])
        else:
            for i in range(idx, length):
                swap(idx, i, combo)
                backtrack(idx + 1, combo)
                swap(idx, i, combo)
    backtrack(0, nums)
    return result

def swap(i, j, nums):
    nums[i], nums[j] = nums[j], nums[i]

nums = [1,2,3]
result = permute(nums)
print(result)