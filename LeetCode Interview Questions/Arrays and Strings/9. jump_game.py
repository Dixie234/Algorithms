from typing import List

def canJump(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    
    result = True
    distance_from_0 = 0 
    for i in range(len(nums) - 2, -1 ,-1):
        if nums[i] == 0:
            distance_from_0 += 1
            result = False
            continue
        if distance_from_0 > 0:
            if nums[i] > distance_from_0:
                result = True
                distance_from_0 = 0
            else:
                result = False
                distance_from_0 += 1
    return result

def canJump_simple(nums: List[int]) -> bool:
    c = 0
    for num in nums:
        if c < 0:
            return False
        elif num > c:
            c = num
        c -= 1
    return True


#nums = [2,3,1,1,4]
nums = [0,1]
result = canJump(nums)
print(result)
                