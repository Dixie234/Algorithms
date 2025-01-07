from typing import List

#Brute force implementation
#Time complexity O(n^2) - Uses nested loop with no break clause therefore is quadratic time
#Space complexity O(n) - Worst case every string is a substring of all other strings in the list, therefore the result would be of n length.
def stringMatching(words: List[str]) -> List[str]:
    return list({word_nested for word in words for word_nested in words if word_nested != word and word_nested in word})
