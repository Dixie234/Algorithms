from typing import List

nums = [1,2,3,3,4,5]

def removeDuplicates(nums: List[int]) -> int:
    length = len(nums)
    if length == 0 or length == 1:
        return length
    
    dupe_offset = 0
    for i in range(length - 1):
        if (nums[i - dupe_offset] != nums[i + 1]):
            nums[(i - dupe_offset) + 1] = nums[i + 1]
        else:
            dupe_offset += 1
    return length - dupe_offset

k = removeDuplicates(nums)
print(k)
print(nums)

def removeDuplicates(nums: List[int]) -> int:
    index = 1
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            nums[index] = nums[i]
            index = index +1
    return index

k = removeDuplicates(nums)
print(k)
print(nums)        


            


    
