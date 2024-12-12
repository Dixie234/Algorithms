from typing import List


def isArrSpecial(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    
    for i in range(1, len(nums)):
        prev = nums[i - 1] % 2 == 0
        curr = nums[i] % 2 == 0
        if prev == curr:
            return False
        
    return True

def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[bool]:
    if len(nums) == 1:
        return [True] * len(queries)
    valid_smallest_start = len(nums)
    valid_largest_end = 0
    invalid_start = 0
    invalid_end = len(nums)
    results = []
    for start, end in queries:
        if start == end:
            results.append(True)
        elif start >= valid_smallest_start and end <= valid_largest_end:
            results.append(True)
        elif start <= invalid_start and end >= invalid_end:
            results.append(False)
        else:
            result = isArrSpecial(nums[start:end + 1])
            if result:
                if start < valid_smallest_start:
                    valid_smallest_start = start
                if end > valid_largest_end:
                    valid_largest_end = end
            else:
                if start > invalid_start:
                    invalid_start = start
                if end < invalid_end:
                    invalid_end = end                
            results.append(result)
    return results

nums = [3,7,3,10,5,5]
queries = [[3,4],[1,5],[5,5],[0,4],[1,2],[2,3],[5,5],[0,1]]
result = isArraySpecial(nums, queries)
print(result)