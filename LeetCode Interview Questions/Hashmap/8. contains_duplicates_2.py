from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    nums_ordinals:dict[int, int] = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in nums_ordinals:
            if (i - nums_ordinals[num]) <= k:
                return True
        nums_ordinals[num] = i
    return False

#[1,0,1,1]
#[1,2,3,1]
#[1,2,3,1,2,3]
nums = [1,2,3,1]
k = 3
result = containsNearbyDuplicate(nums, k)
print(result)