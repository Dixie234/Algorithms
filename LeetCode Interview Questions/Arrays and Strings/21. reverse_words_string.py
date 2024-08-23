
def reverseWords(s: str) -> str:
    s_list = s.split('')
    for i in range(len(s_list) - 1):
        s_list[i] = s_list[i].strip()
    return " ".join(s_list[::-1]).strip()
        