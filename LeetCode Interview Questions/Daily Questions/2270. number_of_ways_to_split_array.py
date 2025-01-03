from typing import List

#Time complexity O(n) - iterate through array twice, once for the initial sum and again inside the loop, O(2n) simplifies to O(n)
#Space complexity O(1) - all variables are integers and therefore only take up constant space
def waysToSplitArray(nums: List[int]) -> int:
    right_total = sum(nums)
    left_total = 0
    valid_splits = 0
    for i in range(len(nums) - 1):
        left_total += nums[i]
        right_total -= nums[i]
        if left_total >= right_total:
            valid_splits += 1
    return valid_splits

