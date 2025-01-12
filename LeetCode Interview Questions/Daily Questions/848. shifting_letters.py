from itertools import accumulate
from typing import List


def shiftingLetters(s: str, shifts: List[int]) -> str:
    cum_shifts = list(accumulate(shifts[::-1]))

    minimum = ord("a")
    maximum = ord("z")
    result = ""
    for i in range(len(s)):
        letter_ord = ord(s[i])
        shift_length = cum_shifts[-(i + 1)] % 26
        new_letter_ord = letter_ord + shift_length
        if new_letter_ord > maximum:
            new_letter_ord = minimum + (new_letter_ord - (maximum + 1))
        result += chr(new_letter_ord)
    return result

s = "abc"
shifts = [3,5,9]
totals = [17, 14, 9]