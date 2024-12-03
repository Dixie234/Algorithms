from typing import List


def addSpaces(s: str, spaces: List[int]) -> str:
    set_space = set(spaces)
    result = ""
    for i, char in enumerate(s):
        if i in set_space:
            result += " " + char
        else:
            result += char
    return result