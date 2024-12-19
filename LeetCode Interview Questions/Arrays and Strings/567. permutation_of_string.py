def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    
    offset = ord("a")
    s1_arr = [0] * 26
    for char in s1:
        s1_arr[ord(char) - offset] += 1

    left = 0
    right = len(s1) - 1
    s2_arr = [0] * 26
    for i in range(left, right):
        s2_arr[ord(s2[i]) - offset] += 1

    for i in range(len(s2) - right):
        s2_arr[ord(s2[right + i]) - offset] += 1
        if s1_arr == s2_arr:
            return True     
        s2_arr[ord(s2[left + i]) - offset] -= 1

    return False

s1 = "ab"
s2 = "eidbaooo"
result = checkInclusion(s1, s2)
print(result)

