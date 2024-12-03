from typing import List


def minimumMountainRemovals(nums: List[int]) -> int:
    length = len(nums)
    left_side = [False] * length
    right_side = [False] * length

    for i in range(len(nums)):
        if i < (length - 1):
            if nums[i] < nums[i + 1]:
                left_side[i] = True
        if i > 0:
            if nums[i] < nums[i - 1]:
                right_side[i] = True

    min_moves = length
    for i in range(1, len(nums) - 1):
        curr = left_side[:i].count(False) + right_side[i + 1:].count(False)
        if curr < min_moves:
            min_moves = curr

    return min_moves

nums = [3,5,6,4,3,5,6,3,2,1,2,3,1]
result = minimumMountainRemovals(nums)

