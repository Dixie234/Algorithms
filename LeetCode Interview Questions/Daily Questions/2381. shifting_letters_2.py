from typing import List

#Uses a difference array for efficent range updates to an array
def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    shifts_diff = [0] * len(s)

    for start, end, direction in shifts:
        shift = 1 if direction else -1
        shifts_diff[start] += shift
        if end + 1 < len(s):
            shifts_diff[end + 1] += -(shift)

    # shifts_diff2 = [0] * len(s)
    # for shift in shifts:
    #     if shift[2] == 1:  
    #         shifts_diff2[shift[0]] += 1  
    #         if shift[1] + 1 < n:
    #             shifts_diff2[shift[1] + 1] -= 1  
    #     else: 
    #         shifts_diff2[shift[0]] -= 1  
    #         if shift[1] + 1 < n:
    #             shifts_diff2[shift[1] + 1] += 1

    total_shift = 0
    result = ""
    minimum = ord("a")
    for i, char in enumerate(s):
        total_shift = (total_shift + shifts_diff[i]) % 26
        if total_shift < 0:
            total_shift += 26
        index = ord(char) - minimum
        shifted_char = chr(minimum + (index + total_shift) % 26)

        result += shifted_char

    return result

s = "dztz"

shifts = [[0,0,0],[1,1,1]]
result = shiftingLetters(s, shifts)
print(result)