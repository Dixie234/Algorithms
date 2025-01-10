from typing import List

#Time complexity O(n * m) - have to iterate over all n words, and the comparison is m length, therefore O(n * m)
#Space complexity O(1) - Just returns an integer, therefore constant space
def prefixCount(words: List[str], pref: str) -> int:
    return sum([word.startswith(pref) for word in words])