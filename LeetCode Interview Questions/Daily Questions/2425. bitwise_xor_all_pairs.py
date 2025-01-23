from typing import List

#Brute force approach
def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    result = 0
    for num1 in nums1:
        for num2 in nums2:
            xor = num1 ^ num2
            result ^= xor

    return result

#The Order in which you XOR elements doesn't matter.
#If the array you're comparing with is even, then it's contents doesn't matter.
#Therefore, check the pairing arrays length, and only include the XOR if it's odd.
#Time Complexity O(n + m) - Worst case both array are odd length, so have to iterate through both arrays
#Space Complexity O(1) - Only stores result integer, therefore constant space
def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    result = 0
    if len(nums2) % 2 == 1:
        for num in nums1:
            result ^= num
    if len(nums1) % 2 == 1:
        for num in nums2:
            result ^= num
        
    return result