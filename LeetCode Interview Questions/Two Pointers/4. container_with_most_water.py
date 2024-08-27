from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    result = 0
    while left <= right:
        left_val = height[left]
        right_val = height[right]
        distance = right - left
        if left_val >= right_val:
            result = max(result, (right_val * distance))
            right -= 1
        else:
            result = max(result, (left_val * distance))
            left += 1
    return result
#[1,8,6,2,5,4,8,3,7]
#[1,1]
heights = [1,8,6,2,5,4,8,3,7,6,5,3,6,4,2,4,5,7,8,4,2,4,6,2,5,6,2]
result = maxArea(heights)
print(result)
