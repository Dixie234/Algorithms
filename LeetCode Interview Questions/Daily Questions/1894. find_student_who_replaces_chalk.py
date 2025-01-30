from typing import List


def chalkReplacer(chalk: List[int], k: int) -> int:
    total = sum(chalk)
    remainder = k % total
    index = 0
    while remainder >= 0:
        if remainder - chalk[index] < 0:
            break
        remainder -= chalk[index]
        index += 1
    return index