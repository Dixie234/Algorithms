def isSubsequence(s: str, t: str) -> bool:
    t_pos = 0
    for char in s:
        t_pos = t.find(char, t_pos)
        if t_pos == -1:
            return False
        else:
            t_pos += 1
    return True

s = "aaaaaa"
t = "bbaaaa"

result = isSubsequence(s, t)
print(result)