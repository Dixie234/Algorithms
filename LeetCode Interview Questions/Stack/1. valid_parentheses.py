from collections import deque


def isValid(s: str) -> bool:
    if len(s) == 1:
        return False
    mapping = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if not stack:
                return False
            check = stack.pop()
            if char != mapping[check]:
                return False
    return not stack

