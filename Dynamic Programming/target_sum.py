from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
    length = len(nums)
    dp = {}
    def find_target(nums, i, target):
        if (i, target) in dp:
            return dp[(i, target)]
        if target == 0 and i == length:
            return 1
        elif i == length:
            return 0
        take_positive = find_target(nums, i + 1, target + nums[i])
        take_negative = find_target(nums, i + 1, target - nums[i])
        dp[(i, target)] = take_positive + take_negative
        return dp[(i, target)]
    return find_target(nums, 0, target)

nums = [1,1,1,1,1]
target = 3