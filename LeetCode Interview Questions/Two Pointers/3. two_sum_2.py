from typing import List

# 2 pointers, if the total is greater than the target, reduce the right pointer by 1, 
# if total is less the target, increase the left pointer by 1,
# else return the answer because target == total.
def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while right >= left:
        total = numbers[left] + numbers[right]
        if total > target:
            right -= 1
        elif total < target:
            left += 1
        else:
            return [left + 1, right + 1]
    return -1


def twoSum_unordered(numbers: List[int], target: int) -> List[int]:
    nums_dict = {element:index  for index, element in enumerate(numbers)}
    for i, num in enumerate(numbers):
        diff = target - num
        if diff in nums_dict and i != nums_dict[diff]:
            return [i + 1, nums_dict[diff] + 1]


#target = 10
# diff = 6
# numbers[med] = 4       
def twoSum_complicated(numbers: List[int], target: int) -> List[int]:
    low = 0
    high = len(numbers) - 1
    previous_vals = {}
    diff_low = 0
    diff_high = 0
    while (high >= low):
        diff_low = target - numbers[low]
        diff_high = target - numbers[high]
        if numbers[low] + numbers[high] == target:
            return [low + 1, high + 1]
        if high == low:
            val = previous_vals[diff_high]
            if val < high:
                return [val + 1, high + 1]
            else:
                return [high + 1, val + 1]
        elif diff_low in previous_vals:
            val = previous_vals[diff_low]
            if val < low:
                return [val + 1, low + 1]
            else:
                return [low + 1, val + 1]
        elif diff_high in previous_vals:
            val = previous_vals[diff_high]
            if val < low:
                return [val + 1, high + 1]
            else:
                return [high + 1, val + 1]
        else:
            previous_vals[numbers[low]] = low
            previous_vals[numbers[high]] = high
            low += 1
            high -= 1
    return -1

#
#[5,25,75]
#[2,7,11,15]
#[12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
#[3,24,50,79,88,150,345]
numbers = [3,24,50,79,88,150,345]
target = 200
result = twoSum(numbers, target)
print(result)
