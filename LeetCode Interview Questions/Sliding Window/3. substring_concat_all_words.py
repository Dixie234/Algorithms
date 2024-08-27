from collections import Counter
from typing import List

def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    # all string words the same length
    ret = []
    n = len(s)
    k = len(words)
    m = len(words[0])
    p = m * k # total len of words
    initWindow = []
    notValid = set()
    valid = set()

    if n < p:
        # dont have enough words
        return []

    for i in range(p):
        letter = s[i]
        initWindow.append(letter)

    if validSubtring("".join(initWindow), p, m):
        ret.append(0)

    i = p
    
    while i < n:
        letter = s[i]
        initWindow.pop(0)
        initWindow.append(letter)
        tempString = "".join(initWindow)
        # use caching here so no need to travsert again
        if tempString not in notValid:
            if tempString in valid or validSubtring(tempString, p, m):
                ret.append(i - p + 1)
                valid.add(tempString)
            else:
                notValid.add(tempString)

        i += 1
    
    return ret

def validSubtring(substring, p, m):
    tempWords = words[:]
    i = 0
    while i < p:
        currWord = substring[i: i + m]
        if currWord in tempWords:
            tempWords.remove(currWord)
        i += m
    
    return tempWords == []

def findSubstring_slow(s: str, words: List[str]) -> List[int]:
    word_length = len(words[0])
    words_required = Counter(words)
    left = 0
    right = word_length
    result = []
    while left <= len(s) - (word_length * len(words)):
        s_word = s[left:right]
        if containsSubstring(s, words, left, right, word_length, s_word, words_required):
            result.append(left)
        left += 1
        right += 1
    return result

def containsSubstring(s, words, left, right, word_length, s_word, words_required):
    words_found = [s_word]
    left += word_length
    right += word_length
    match = True
    while match and len(words_found) != len(words):
        s_word = s[left:right]
        if s_word in words_required:
            words_found.append(s_word)
            left += word_length
            right += word_length
        else:
            match = False
    return words_required == Counter(words_found)


#s = "barbarfoothefoobarmanbar"
#s = "barfoofoobarthefoobarman"
s = "barfoothefoofoobarfoobarman"
# s = "aaaaaaaaa"
#s = "ababaab"#
words = ["foo","bar","foo"]
#words = ["aa","aa"]
#words = ["ab","ba","ba"]
result = findSubstring(s, words)
print(result)

