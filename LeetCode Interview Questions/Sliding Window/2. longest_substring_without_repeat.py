def lengthOfLongestSubstring(s: str) -> int:
    result = 0
    slow = 0
    chars = {}
    duplicates = 0
    for fast, char in enumerate(s):
        if char in chars and chars[char] > 0:
            chars[char] += 1
            duplicates += 1
        else:
            chars[char] = 1
        while duplicates > 0:
            s_slow = s[slow]
            chars[s_slow] -= 1
            if chars[s_slow] == 1:
                duplicates -= 1
            slow += 1
        result = max(result, (fast - slow) + 1)
    return result

def lengthOfLongestSubstring_using_set(s: str) -> int:
    n = len(s)
    maxLength = 0
    charSet = set()
    left = 0
    
    for right in range(n):
        if s[right] not in charSet:
            charSet.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        else:
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
    
    return maxLength

#s = "abcabcbb"
#s = "bbbbbb"
#s = "pwwkew"
#s = "abcabcd"
#s = "abcccccab"
s = "jbjaabfaaabajgbaaaaacabd"
result = lengthOfLongestSubstring(s)
print(result)