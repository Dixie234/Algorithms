from typing import List


def maxCount(banned: List[int], n: int, maxSum: int) -> int:
    banned_set = set(banned)
    total = 0
    nums = 0
    for i in range(1, n + 1):
        if i not in banned_set:
            if (total + i) > maxSum:
                break
            else:
                total += i
                nums += 1

    return nums
