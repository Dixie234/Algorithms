from itertools import combinations
from typing import List


def findDifferentBinaryString(nums: List[str]) -> str:
    length = len(nums[0])
    if length == 1:
        if nums[0] == "1":
            return "0"
        else:
            return "1"
        
    nums_set = set([int(num, 2) for num in nums])
    possible_nums = (length ** 2) - 1
    encoding = '0' + str(length) + 'b'
    
    for i in range(possible_nums):
        if i not in nums_set:
            return str(format(i, encoding))


