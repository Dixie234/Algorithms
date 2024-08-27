from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    result = None
    total = 0
    slow = 0
    for fast, num in enumerate(nums):
        total += num
        while total >= target:
            distance = (fast - slow) + 1
            if not result:
                result = distance
            else:
                result = min(result, distance)
            total -= nums[slow]
            slow += 1
    return result if result else 0

#nums = [7,2,3,1,2,4,3,7,7,7]
nums = [4,5,5,5,5,5]
target = 25
result = minSubArrayLen(target, nums)
print(result)