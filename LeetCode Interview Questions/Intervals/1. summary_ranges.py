from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    result = []
    nums.append(nums[len(nums) - 1] + 2) #append extra value to ensure loop include final value
    start = nums[0]
    stop = None
    for i in range(len(nums) - 1):
        current = nums[i]
        next = nums[i + 1]
        if nums[i + 1] - current > 1:
            stop = current
            if start == stop:
                result.append(f"{start}")
            else:
                result.append(f"{start}->{stop}")
            start = next
    return result

def summaryRanges_nested(nums: List[int]) -> List[str]:
    if nums == []:
        return []

    output = []
    i = 0
    while i < len(nums):
        start = nums[i] #store initial value of i
        while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
            i += 1
        
        if start == nums[i]:
            output.append(f"{start}")
        else:
            output.append(f"{start}->{nums[i]}")
        
        i += 1
    
    return output
    
nums = [0,1,2,4,5,7]
result = summaryRanges(nums)
print(result)


