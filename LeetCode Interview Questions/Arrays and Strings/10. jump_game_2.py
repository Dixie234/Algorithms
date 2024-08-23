from typing import List

nums = [2,3,1,1,4]
nums = [2,3,0,1,4]

def jump(nums: List[int]) -> int:
    total = len(nums) - 1
    steps = 0
    index = 0
    while total > 0:
        max_val = 1
        index_jump = 1
        for i in range(1, nums[index] + 1):
            if index + i >= len(nums) - 1:
                return steps + 1
            if nums[index + i] + i > max_val:
                max_val = nums[index + i] + i
                index_jump = i
        total -= index_jump
        steps += 1
        index += index_jump
        
    return steps


nums = [0]
nums = [2,3,0,1,4]
nums = [2,3,5,1,2,5,3,5,6,3,2,5,6,6,0]

length = 12
target = 11

result = jump(nums)
print(result)

