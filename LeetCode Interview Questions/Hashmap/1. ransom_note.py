from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    letters = Counter(magazine)
    for char in ransomNote:
        if char not in letters:
            return False
        else:
            if letters[char] <= 0:
                return False
            else:
                letters[char] -= 1
    return True

a = "aaa"
b = "abbaa"

result = canConstruct(a, b)
print(result)