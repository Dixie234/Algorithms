def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

haystack = "sadbutsad"

needle = "sad"

result = strStr(haystack, needle)
print(result)