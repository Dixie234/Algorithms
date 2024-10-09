from typing import List


def plusOne(digits: List[int]) -> List[int]:
    length = len(digits)
    if digits[-1] != 9:
        digits[-1] = digits[-1] + 1
    else:
        for i in range(length):
            if digits[-(1 + i)] == 9:
                digits[-(1 + i)] = 0
            else:
                digits[-(1 + i)] = digits[-(1 + i)] + 1
                break
        if sum(digits) == 0:
            digits[0] = 1
            digits.append(0)
    return digits
        
                
        