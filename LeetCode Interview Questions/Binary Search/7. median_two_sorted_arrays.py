from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums1_length = len(nums1)
    nums2_length = len(nums2)  

    if nums2_length == 0:
        length = nums1_length
        if length % 2 == 0:
            return (nums1[length // 2] + nums1[(length // 2) - 1]) / 2
        else:
            return nums1[(length // 2)]


    total_len = nums1_length + nums2_length
    mid = total_len // 2

    i_nums1 = 0
    i_nums2 = 0
    total = 0
    comb_nums = []
    while total <= mid:
        if i_nums1 >= nums1_length:
            value = nums2[i_nums2]
            i_nums2 += 1
        elif i_nums2 >= nums2_length:
            value = nums1[i_nums1]
            i_nums1 += 1             
        elif nums1[i_nums1] <= nums2[i_nums2]:
            value = nums1[i_nums1]
            i_nums1 += 1
        else:
            value = nums2[i_nums2]
            i_nums2 += 1
        total += 1
        if total >= mid:
            comb_nums.append(value)

    if total_len % 2 == 0:
        result = (comb_nums[1] + comb_nums[0]) / 2
    else:
        result = comb_nums[1]

    return result

#using binary search across the 2 arrays
def findMedianSortedArrays(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    
    # Ensure nums1 is the smaller array for simplicity
    if n1 > n2:
        return findMedianSortedArrays(nums2, nums1)
    
    n = n1 + n2
    left = (n1 + n2 + 1) // 2 # Calculate the left partition size
    low = 0
    high = n1
    
    while low <= high:
        mid1 = (low + high) // 2 # Calculate mid index for nums1
        mid2 = left - mid1 # Calculate mid index for nums2
        
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        
        # Determine values of l1, l2, r1, and r2
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]
        
        if l1 <= r2 and l2 <= r1:
            # The partition is correct, we found the median
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Move towards the left side of nums1
            high = mid1 - 1
        else:
            # Move towards the right side of nums1
            low = mid1 + 1
    
    return 0 # If the code reaches here, the input arrays were not sorted.
