from typing import List

#offset = 4
#[1,2,3,4,5]
#         ^
#rotates the array to the left a number of steps
def rotLeft(a:List[int], d:int) -> List[int]:
    length = len(a)
    offset = d % length
    result = [0] * length
    for i, num in enumerate(a):
        new_i = i - offset
        if new_i < 0:
            new_i += length
        result[new_i] = num
    return result

#rotates the array to the right a number of steps
def rotRight(a:List[int], d:int) -> List[int]:
    length = len(a)
    offset = d % length
    result = [0] * length
    for i, num in enumerate(a):
        new_i = i + offset
        if new_i >= length:
            new_i -= offset + 1
        result[new_i] = num
    return result

