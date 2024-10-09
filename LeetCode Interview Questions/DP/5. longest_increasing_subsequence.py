from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    res = []

    for num in nums:
        if not res or num > res[-1]:
            res.append(num)
        else:
            i = binary_search(res, num)
            res[i] = num
    return len(res)


def binary_search(arr, x):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left

result = lengthOfLIS([11,12,13,14,15,5,6,7,8,9,10,11])
print(result)