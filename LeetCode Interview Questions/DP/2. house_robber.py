from typing import List


def rob(nums: List[int]) -> int:
    total = []
    prev_index = -1
    i = 1
    while i < len(nums):
        prev = nums[i - 1]
        current = nums[i]

        if prev >= current:
            if prev_index != i - 1:
                total.append(prev)
            prev_index = i - 1
        else:
            nums_prev = nums[prev_index]
            if (nums_prev + current) > prev:
                total.pop()
                total.append(nums_prev)
            total.append(current)
            prev_index = i

        i += 1
    return sum(total)


nums = [2,1,9,1,1,8,1,7,1,1,1,8,1,1,9,1,1,7]
result = rob(nums)
print(result)