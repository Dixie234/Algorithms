from typing import List

nums = [3,2,3]

def majorityElement(nums: List[int]) -> int:
    counts = dict()

    for num in nums:
        if(num in counts):
            counts[num] += 1
        else:
            counts[num] = 1
    for key, value in counts.items():
        if(value > (len(nums) / 2)):
            return key

result = majorityElement(nums)
print(result)


    
    

