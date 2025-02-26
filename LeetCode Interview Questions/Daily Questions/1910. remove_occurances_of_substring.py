def removeOccurrences(s: str, part: str) -> str:
    if s == part:
        return ""
    part_length = len(part)

    while part in s:
        left = 0
        updated_s = ""
        s_length = len(s)
        if s[left] == part[0]:
            part_check = left + part_length
            if part_check <= s_length:
                if s[left:part_check] == part:
                    left = part_check
                    break
        s = updated_s
    return s

s = "aabababa"
part = "aba"
result = removeOccurrences(s, part)
print(result)
                

