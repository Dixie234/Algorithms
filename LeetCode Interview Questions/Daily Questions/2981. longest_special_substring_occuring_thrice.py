from collections import Counter


def maximumLength(s: str) -> int:
    s_counts = Counter(s)
    possible_chars = []
    for k, v in s_counts.items():
        repeat_num = v // 3
        if repeat_num > 0:
            possible_chars.append(k)

    if len(possible_chars) == 0:
        return -1
    
    max_char_length = 1
    for char in possible_chars:
        curr_char_length = 1
        for i in range(2, len(s)):
            curr_str = char * i
            found = 0
            left = 0
            right = i
            while right <= len(s):
                s_sub_string = s[left:right]
                if curr_str == s_sub_string:
                    found += 1
                left += 1
                right += 1
            if found < 3:
                break
            else:
                curr_char_length = i
        if curr_char_length > max_char_length:
            max_char_length = curr_char_length
    return max_char_length

s = "aaaa"
result = maximumLength(s)
print(result)

def maximumLength(s: str) -> int:
    n = len(s)
    l, r = 1, n

    if not helper(s, n, l):
        return -1

    while l + 1 < r:
        mid = (l + r) // 2
        if helper(s, n, mid):
            l = mid
        else:
            r = mid

    return l

def helper(s: str, n: int, x: int) -> bool:
    cnt = [0] * 26
    p = 0

    for i in range(n):
        while s[p] != s[i]:
            p += 1
        if i - p + 1 >= x:
            cnt[ord(s[i]) - ord('a')] += 1
        if cnt[ord(s[i]) - ord('a')] > 2:
            return True

    return False

s = "aaaabbb"
result = maximumLength(s)
print(result)




