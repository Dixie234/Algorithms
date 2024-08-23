def wordPattern(pattern: str, s: str) -> bool:
    s_list = s.split(" ")
    length = len(s_list)
    if length != len(pattern):
        return False
    pattern_mapping = {}
    for i in range(length):
        if s_list[i] in pattern_mapping:
            if pattern_mapping[s_list[i]] != pattern[i]:
                return False
        else:
            if pattern[i] in pattern_mapping.values():
                return False
            else:
                pattern_mapping[s_list[i]] = pattern[i]
    return True

pattern = "abba"
s = "dog cat cat dog"
result = wordPattern(pattern, s)
print(result)



