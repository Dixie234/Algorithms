from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    low = 0
    high = len(matrix) - 1
    while low <= high:
        mid = (low + high) // 2
        found, index = binary_search(matrix[mid], target)
        if found:
            return True
        elif index == 0:
            high = mid - 1
        else:
            low = mid + 1
    return False

def binary_search(nums, val):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == val:
            return True, mid
        elif nums[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return False, low

nums = [1,2,3,4]
num = 0
result = binary_search(nums, num)
print(result)