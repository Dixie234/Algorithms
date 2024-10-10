from typing import List


def findMin(nums: List[int]) -> int:
    start = nums[0]
    end = nums[-1]
    is_rotated = start > end
    if is_rotated:
        result = find_arr_start(nums, start)
    else:
        result = 0
    return nums[result]

def find_arr_start(nums, start):
    if len(nums) == 2:
        return 1
    
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2

        left_val = float("inf")
        if mid != 0:
            left_val = nums[mid - 1]
        right_val = float("inf")
        if mid + 1 != len(nums):
            right_val = nums[mid + 1]
        
        if nums[mid] < left_val and nums[mid] < right_val:
            return mid
        elif nums[mid] >= start:
            low = mid + 1
        else:
            high = mid - 1
    return low
