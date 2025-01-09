from typing import List


def prefixCount(words: List[str], pref: str) -> int:
    return sum([word.startswith(pref) for word in words])