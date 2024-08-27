from collections import Counter
import math


def minWindow(s: str, t: str) -> str:
    counts = { v: 0 for k, v in enumerate(list(t)) }
    required_counts = Counter(t)
    missing = len(t)
    substring_indexes = (-1, 999999999)
    fast = 0
    slow = 0
    for char in s:
        if char in counts:
            if counts[char] < required_counts[char]:
                missing -= 1
            counts[char] += 1
        fast += 1
        if missing == 0:
            while missing == 0:
                if (fast - slow) < (substring_indexes[1] - substring_indexes[0]):
                    substring_indexes = (slow, fast)
                slow_s = s[slow]
                if slow_s in counts:
                    if counts[slow_s] == required_counts[slow_s]:
                        missing += 1
                    counts[slow_s] -= 1
                slow += 1
    return "" if substring_indexes[0] == -1 else s[substring_indexes[0]: substring_indexes[1]]


s = "cabwefgewcwaefgcf"
t = "cae"
result = minWindow(s, t)
print(result)