from typing import List

nums1 = [0,0,0,0,0]
m = 0
nums2 = [1,2,3,5,6]
n = 5

# nums1 = [1,2]
# m = 2
# nums2 = []
# n = 0

# nums1 = [1,2,4,0,0,0]
# m = 3
# nums2 = [2,3,5]
# n = 3

# nums1 = [1,4,6]
# m = 3
# nums2 = []
# n = 0

# nums1 = [2,4,5,7,8,9,11,12,0,0,0,0,0,0,0,0,0]
# m = 8
# nums2 = [1,2,5,6,7,8,9,11,15]
# n = 9

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:    
    a = m - 1
    b = n - 1
    c = (m + n) - 1

    while b > -1:
        if((nums2[b] > nums1[a]) or (a == -1)):
            nums1[c] = nums2[b]
            c -= 1
            b -= 1
        else:
            nums1[c] = nums1[a]
            nums1[a] = 0
            c -= 1
            a -= 1

merge(nums1, m, nums2, n)

nums1

# nums2[::-1]
