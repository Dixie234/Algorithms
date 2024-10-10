from typing import List

#[5,7,7,8,8,10]
def searchRange(nums: List[int], target: int) -> List[int]:
    target_index = binary_search(nums, target)
    if target_index == -1:
        return -1
    
    left_start = binary_left_search(nums, target, target_index)
    right_start = binary_right_search(nums, target, target_index)
    return [left_start, right_start]
    
def binary_left_search(nums, target, right_index):
    if right_index == 0:
        return 0
    
    low = 0
    high = right_index
    while low <= high:
        mid = (low + high) // 2

        left_val = float("-inf")
        if mid != 0:
            left_val = nums[mid - 1]

        if nums[mid] == target and left_val < nums[mid]:
            return mid
        elif nums[mid] == target and left_val == target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def binary_right_search(nums, target, left_index):
    length = len(nums) - 1
    if left_index == length:
        return length
    
    low = left_index
    high = length
    while low <= high:
        mid = (low + high) // 2

        right_val = float("inf")
        if mid != length:
            right_val = nums[mid + 1]

        if nums[mid] == target and right_val > nums[mid]:
            return mid
        elif nums[mid] == target and right_val == target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

nums = [5,7,7,8,8,10]
target = 8