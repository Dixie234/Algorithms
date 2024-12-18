from typing import List

#Use of hash map to reduce repeated lookups to O(n)
#However, brute force approach to scanning secondary array for each nums1 value to see if greater value exists.
#Time complexity O(n * m) - Where n and m are the respective lengths of nums1 and nums2
#Space complexity O(n + m) - Hash map of nums2, and resulting array the size of nums1
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nums2_map = {val: index for index, val in enumerate(nums2)}
    result = [-1] * len(nums1)
    for i, val in enumerate(nums1):
        for j in range(nums2_map[val], len(nums2)):
            if nums2[j] > val:
                result[i] = nums2[j]
                break
    return result

#Optimized search using monotonic stack to more quickly identify greater than values
#Uses a hashmap of nums1 for O(1) lookups each time it finds a greater than value
#Time complexity O(n + m) - It iterates through nums1 to create the hashmap, and through nums2 to identify each greater than value
#Space complexity O(n + m) - Hash map of nums1, and resulting array the size of nums1, and stack of worse case nums2 size
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_map = {val: index for index, val in enumerate(nums1)}
    stack = []
    result = [-1] * len(nums1)
    for i, val in enumerate(nums2):
        while stack and nums2[stack[-1]] < val:
            prev_val = nums2[stack.pop()]
            if prev_val in nums1_map:
                result[nums1_map[prev_val]] = val
        stack.append(i)

    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
result = nextGreaterElement(nums1, nums2)
print(result)