from collections import deque
from typing import List

digit_mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    result = []
    length = len(digits)
    def backtrack(idx, combo):
        nonlocal result, length
        
        if idx == length:
            result.append(combo)
        else:
            for letter in digit_mapping[digits[idx]]:
                backtrack(idx + 1, combo + letter)
    backtrack(0, "")
    return result


digits = "23"
result = letterCombinations(digits)
print(result)