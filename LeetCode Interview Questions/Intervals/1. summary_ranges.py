from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    result = []
    nums.append(nums[len(nums) - 1] + 2)
    start = nums[0]
    stop = None
    for i in range(len(nums) - 1):
        current = nums[i]
        next = nums[i + 1]
        if nums[i + 1] - current > 1:
            stop = current
            if start == stop:
                result.append(f"{start}")
            else:
                result.append(f"{start}->{stop}")
            start = next
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


