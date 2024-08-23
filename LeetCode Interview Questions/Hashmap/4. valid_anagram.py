def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def isAnagram_slow(s: str, t: str) -> bool:
    if not len(s) == len(t):
        return False
    dic = {item: s.count(item) for item in s}
    for char in t:
        if char not in dic:
            return False
        else:
            if dic[char] == 1:
                dic.pop(char)
            else:
                dic[char] -= 1
    return len(dic) == 0