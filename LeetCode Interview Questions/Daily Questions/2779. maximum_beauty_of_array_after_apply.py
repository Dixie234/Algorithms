from typing import List

#sliding window of sorted values
#as the range falls outside of overlapping, move the left pointer along until they match again
#compare the existing max_overlaps with the current overlaps by comparing the left and right indexes
#ensure to + 1 to compare to account for when indexes are equal
def maximumBeauty(nums: List[int], k: int) -> int:
    nums.sort()
    max_overlaps = 0
    left = 0
    for right in range(len(nums)):
        left_range = (nums[left] - k, nums[left] + k)
        right_range = (nums[right] - k, nums[right] + k)
        while not is_overlap(left_range, right_range):
            left += 1
            left_range = (nums[left] - k, nums[left] + k)
   
        max_overlaps = max(max_overlaps, (right - left) + 1)

    return max_overlaps

def is_overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

l = [4,6,1,2]
k = 2
result = maximumBeauty(l, k)
print(result)

