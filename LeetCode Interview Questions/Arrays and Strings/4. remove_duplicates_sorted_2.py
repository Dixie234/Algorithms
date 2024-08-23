from typing import List

nums = [0, 0, 0]

def removeDuplicates(nums: List[int]) -> int:
    length = len(nums)
    
    dupe_offset = 0
    dupe_counter = 0
    for i in range(length - 1):
        if (nums[i - dupe_offset] == nums[i + 1]):
            if(dupe_counter > 0):
                dupe_offset += 1
            nums[(i - dupe_offset) + 1] = nums[i + 1]
            dupe_counter += 1
        else:
            nums[(i - dupe_offset) + 1] = nums[i + 1]
            dupe_counter = 0
    return length - dupe_offset 

k = removeDuplicates(nums)
print(k)
print(nums)

def removeDuplicates(nums: List[int]) -> int:
    index = 1
    occurance = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            occurance += 1
        else:
            occurance = 1
        if occurance <= 2:
            nums[index] = nums[i]
            index += 1
    
    return index