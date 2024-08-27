from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    i = 0
    j = i + 1
    k = len(nums) - 1
    prev_i = None
    result = []
    while j < k:
        if nums[i] == prev_i:
            i += 1
            j += 1
            continue
        triplets = findTriplets(nums, i, j, k)
        if len(triplets) > 0:
            result.extend(triplets)
        prev_i = nums[i]
        i += 1
        j += 1
    return [list(groups) for groups in result]
        

def findTriplets(nums, i, j, k):
    result = set()
    num_i = nums[i]
    while j < k:
        num_j = nums[j]
        num_k = nums[k]
        triplet = (num_i, num_j, num_k)
        total = sum(triplet)
        if total > 0:
            k -= 1
        elif total < 0:
            j += 1
        else:
            result.add(triplet)
            j += 1
    return result

#nums = [-4,-1,-1,0,1,2]
#nums = [0,0,1]
#nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
result = threeSum(nums)
print(result)