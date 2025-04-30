from typing import List
import math

#use epsilons when dealing with log

def findNumbers(nums: List[int]) -> int:
    result = 0
    for num in nums:
        digits = math.ceil(math.log10(num) + 1e-9)
        if digits % 2 == 0:
            result += 1
    return result

def findNumbers(nums: List[int]) -> int:
    return sum([1 if math.ceil(math.log10(num) + 1e-9) % 2 == 0 else 0 for num in nums])