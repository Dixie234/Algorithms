from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_dict = {element:index  for index, element in enumerate(nums)}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in nums_dict and i != nums_dict[diff]:
            return [nums_dict[diff], i]



nums = [2,7,11,15]
target = 9



