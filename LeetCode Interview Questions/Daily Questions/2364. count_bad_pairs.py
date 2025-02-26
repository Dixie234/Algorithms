from typing import List


def countBadPairs(nums: List[int]) -> int:
    bad_pairs = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i - j == nums[i] - nums[j]:
                bad_pairs += 1
    return bad_pairs

