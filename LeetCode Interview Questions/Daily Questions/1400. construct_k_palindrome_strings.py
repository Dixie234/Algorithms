#Count number of occurances of odd number of characters, if this count is less than or equal to k, then it's possible.
#Includes optimization that because only 26 possible characters, if k exceeds that then it must be true.
#Further optimization would be to use a bitmap instead of an array to track the number of odd occurances.
#Time Complexity O(n) - Iterates over s once and then sum's up the ordinal counter
#Space Complexity O(1) - s_arr takes up constant space of 26 values irrespective of s size, therefore constant space.
def canConstruct(s: str, k: int) -> bool:
    length = len(s)
    if length == k:
        return True
    elif length < k:
        return False
    elif k >= 26:
        return True
    
    s_arr = [0] * 26
    offset = ord("a")
    for char in s:
        s_arr[ord(char) - offset] += 1

    odd_count = sum(1 for char in s_arr if char % 2 == 1)
    return odd_count <= k   