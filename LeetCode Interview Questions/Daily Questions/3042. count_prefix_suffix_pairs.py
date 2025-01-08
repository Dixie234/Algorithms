from typing import List


#Brute force solution
#Time Complexity O(n^2 * m) - nested loop across words, with a O(2m) search through each string on ever iteration
#Space Complexity O(1) - Single variable has constant space
def countPrefixSuffixPairs(words: List[str]) -> int:
    result = 0
    for i, word in enumerate(words):
        for j, word_nested in enumerate(words):
            if i < j and isPrefixSuffix(word, word_nested):
                result += 1
    return result


def isPrefixSuffix(s1:str, s2:str):
    return s2.startswith(s1) and s2.endswith(s1)