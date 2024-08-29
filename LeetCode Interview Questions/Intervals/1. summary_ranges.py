from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    result = []
    prev = nums[0]
    start = nums[0]
    stop = None
    for i in range(1, len(nums)):
        current = nums[i]
        if current - prev > 1:
            stop = prev
            result.append(create_string(start, stop))
            start = nums[i]
        prev = current
    return result

def create_string(start, stop):
    char = "->"
    if start == stop:
        return str(start)
    else:
        return str(start) + char + str(stop)
    
nums = [0,1,2,4,5,7]
result = summaryRanges(nums)
print(result)

