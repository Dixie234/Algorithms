def isPalindrome(x: int) -> bool:
    s = str(x)
    length = len(s)
    if len(s) == 1:
        return True

    start = 0
    end = length - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
        
    return True