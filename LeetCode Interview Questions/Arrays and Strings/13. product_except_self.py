import math
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    total = math.prod(nums)
    zero_count = 0
    result = []
    for i, num in enumerate(nums):
        if num == 0:
            prev_num = nums.pop(i)
            sum_product = math.prod(nums)
            nums.insert(i, prev_num)
            result.append(sum_product)
            zero_count += 1
        elif zero_count > 1:
            return [0 for i in nums]
        else:
            result.append(total // num)
    return result

def productExceptSelf_nodiv(nums: List[int]) -> List[int]:
    n = len(nums)

    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = nums[i - 1] * prefix[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = nums[i + 1] * suffix[i + 1]

    return [prefix[i] * suffix[i] for i in range(n)]


def productExceptSelf_slow(nums: List[int]) -> List[int]:
    result = []
    for i, num in enumerate(nums):
        prev_num = nums.pop(i)
        sum_product = math.prod(nums)
        nums.insert(i, prev_num)
        result.append(sum_product)
    return result

nums = [-1,1,0,-3,3]
result = productExceptSelf_nodiv(nums)
print(result)
        
    