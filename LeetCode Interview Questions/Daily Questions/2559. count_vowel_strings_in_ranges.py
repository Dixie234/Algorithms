from itertools import accumulate
from typing import List

vowels = {"a", "e", "i", "o", "u"}

#Create a cumulative sum of the number of words which start and end with vowels, using a set for the vowels for fast checking
#Combine that with a list starting with 0 to account for off-by-one errors 
#For every query, take the difference between the start and end indexes inside the cumlative sum list
#Time Complexity O(n + m) - Iterates through the words and queries lists once
#Space Complexity O(n) - creates another list of length words 
def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    words_with_vowels = [0]
    words_with_vowels.extend(list(accumulate([1 if word[0] in vowels and word[-1] in vowels else 0 for word in words])))
    result = []
    for start, end in queries:
        result.append(words_with_vowels[end + 1] - words_with_vowels[start])
    return result

#Time limit exceeded due to array slicing on every iteration of queries
def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    words_with_vowels = [True if word[0] in vowels and word[-1] in vowels else False for word in words]
    result = []
    for query in queries:
        result.append(words_with_vowels[query[0]:query[1] + 1].count(True))
    return result