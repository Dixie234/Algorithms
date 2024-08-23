from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    chars = len(min(strs, key = len))
    for i in range(chars):
        for j in range(1, len(strs)):
            if strs[j - 1][i] != strs[j][i]:
                return prefix
        prefix += strs[0][i]
    return prefix

strs = ["flower","flow","flight"]

result = longestCommonPrefix(strs)
print(result)




