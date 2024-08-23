def isPalindrome(s: str) -> bool:
    begin = 0
    end = len(s) -1
    while begin < end:
        if not s[begin].isalnum():
            begin += 1
        if not s[end].isalnum():
            end -= 1
        if s[begin].lower() != s[end].lower():
            return False
        begin += 1
        end -= 1
    return True

s = "aa"

def isPalindrome_simple(s: str) -> bool:
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum()) 
    if s == s[::-1]:
        return True
    else:
        return False

result = isPalindrome(s)
print(result)