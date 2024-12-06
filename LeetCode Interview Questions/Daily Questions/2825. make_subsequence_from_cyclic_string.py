def canMakeSubsequence(str1: str, str2: str) -> bool:
    str1_len = len(str1)
    str2_len = len(str2)
    if str1_len < str2_len:
        return False
    
    str1_i = 0
    str2_i = 0

    while str2_i < str2_len:
        find_char = str2[str2_i]
        while str1_i <= str1_len:
            if str1_i == str1_len:
                return False
            
            curr_char = str1[str1_i]
            next_char = "a" if curr_char == "z" else chr(ord(curr_char) + 1)

            if find_char == curr_char or find_char == next_char:
                str1_i += 1
                str2_i += 1
                break
            else:
                str1_i += 1

    return True
    
