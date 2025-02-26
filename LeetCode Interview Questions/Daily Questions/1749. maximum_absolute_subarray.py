from typing import List

#Naive implementation O(n^2)
def maxAbsoluteSum(nums: List[int]) -> int:
    result = 0
    for i in range(len(nums)):
        curr_sum = nums[i]
        for j in range(i + 1, len(nums)):
            curr_sum += nums[j]
            result = max(abs(curr_sum), result)
    return result

nums = [1,-3,2,3,-4]
result = maxAbsoluteSum(nums)
print(result)

#Alteration of Kadane's algorithm to include tracking of current minimum subarray
#Time Complexity O(n)
#Space Complexity O(1)
def maxAbsoluteSum(nums: List[int]) -> int:
    result = nums[0]
    max_end = nums[0]
    min_end = nums[0]
    for i in range(1, len(nums)):
        max_end = max(max_end + nums[i], nums[i])
        min_end = min(min_end + nums[i], nums[i])
        result = max(abs(min_end), max_end, result)
    return result

nums = [1,-3,2,3,-4]
result = maxAbsoluteSum(nums)
print(result)




