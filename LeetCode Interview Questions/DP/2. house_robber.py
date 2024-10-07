from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    
    prev1 = 0
    prev2 = 0
    for num in nums:
        result = max((prev2 + num), prev1)
        prev2 = prev1
        prev1 = result
    return result

def rob_memoized_recursion(nums: List[int]) -> int:
    memo = {}
    def rob_houses(nums, i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        result = max((rob_houses(nums, i - 2) + nums[i]), rob_houses(nums, i - 1))
        memo[i] = result
        return result
    
    return rob_houses(nums, len(nums) - 1)



nums = [400,2,3,4,5]
result = rob(nums)
print(result)