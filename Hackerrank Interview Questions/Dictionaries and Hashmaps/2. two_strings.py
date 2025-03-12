def twoStrings(s1:str, s2:str):
    if len(s1) < len(s2):
        twoStrings(s2, s1)

    s1_set = { char for char in s1 }
    for char in s2:
        if char in s1_set:
            return "YES"
    return "NO"