from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    
    dist_nums:List[int] = sorted(set(nums))
    max_sequence = 1
    result = 1
    for i in range(len(dist_nums) - 1):
        if dist_nums[i + 1] - dist_nums[i] == 1:
            result += 1
        else:
            if result > max_sequence:
                max_sequence = result
            result = 1
    if result > max_sequence:
        max_sequence = result    
    return max_sequence



nums = [0,3,7,2,5,8,4,6,0,1]
result = longestConsecutive(nums)
print(result)