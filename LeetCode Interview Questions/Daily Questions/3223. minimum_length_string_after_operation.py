#Create an ordinal array of character occurances (could equally use a Counter)
#Take bottom up approach to calculate the numbers of characters that will be left after reducing them as much as possible
#If the number is even, add 2 to the result as that is the lowest even number possible. 
#If the number is odd, add 1 to the result as that is the lowest odd number possible.
#Time Complexity O(n) - n iterations to create ordinal array, then iterating through all letter is 26, therefore constant time.
#Space Complexity O(1) - array is always 26 in length, therefore constant space. 
def minimumLength(s: str) -> int:
    s_arr = [0] * 26
    offset = ord("a")
    for char in s:
        s_arr[ord(char) - offset] += 1

    result = 0
    for char_count in s_arr:
        if char_count == 0:
            continue
        elif char_count % 2 == 0:
            result += 2
        else:
            result += 1
    return result

s = "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"
sresult = minimumLength(s)