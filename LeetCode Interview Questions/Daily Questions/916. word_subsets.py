from typing import List

#Turn words 2 into a single word using the maximum amount of occurances of each letter in each word of words2
#Convert words1 into a ordinal array and then ensure that the array fits within the words2_arr
#Time Complexity O(n + m) - where n and m and the total characters in words1 and words2. Iterates over every letter for O(26 *(n + m)) which simplifies O(n + m)
#Space Complexity O(n) - maximum result length is all words in words1, and words1_arr is of length words1. All other arrays are constant space of 26.
def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    words2_arr = [0] * 26
    ord_offset = ord("a")
    for word in words2:
        for i, char in enumerate(word):
            words2_arr[i] = max(word_arr[i], words2_arr[i])

    words1_arr = [[0] * 26 for _ in range(len(words1))]
    for i, word in enumerate(words1):
        for char in word:
            words1_arr[i][ord(char) - ord_offset] += 1

    result = []
    for i, word_arr in enumerate(words1_arr):
        is_universal = True
        for j in range(26):
            if word_arr[j] < words2_arr[j]:
                is_universal = False
                break
        if is_universal:
            result.append(words1[i])

    return result

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]
result = wordSubsets(words1, words2)
print(result)

        


    