from typing import List


def findPeakElement(nums: List[int]) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        left_num = float("-inf")
        if mid - 1 > -1:
            left_num = nums[mid - 1]
        right_num = float("-inf")
        if mid + 1 < len(nums):
            right_num = nums[mid + 1]
        if nums[mid] > left_num and nums[mid] > right_num:
            return mid
        elif nums[mid] > right_num:
            high = mid - 1
        else:
            low = mid + 1
    return low