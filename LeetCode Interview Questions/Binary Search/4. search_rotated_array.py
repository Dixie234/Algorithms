from typing import List

#[4,5,6,7,0,1,2,3]
#[6,7,0,1,2,3,4,5]
#[1,2,3,4,5,6,7,0]
#[3,1]
def search(nums: List[int], target: int) -> int:
    start = nums[0]
    end = nums[-1]
    is_rotated = start > end
    if is_rotated:
        offset = find_arr_start(nums, start)
        result = offset_binary_search(nums, target, offset)
    else:
        result = binary_search(nums, target)
    return result

#simple solution using comparison to tell if in order or not
def search(nums: List[int], target: int) -> int:

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def offset_binary_search(nums, target, offset):
    low = 0
    length = len(nums)
    high = length - 1
    while low <= high:
        mid = (low + high) // 2
        offset_index = get_arr_val(mid, offset, length)
        if nums[offset_index] == target:
            return offset_index
        elif nums[offset_index] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

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


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

#[4,5,6,7,0,1,2,3]
#[6,7,0,1,2,3,4,5]
#[1,2,3,4,5,6,7,0]
def get_arr_val(index, offset, arr_length):
    if (index + offset) > (arr_length - 1):
        ori_index = (index + offset) - arr_length
    else:
        ori_index = index + offset
    return ori_index

nums = [5,1,2,3,4]
target = 1
result = search(nums, target)
print(result)
