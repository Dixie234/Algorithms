from typing import List


def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    result = []
    set_a = [0] * len(A)
    for i in range(len(A)):
        start_val = 0 if i == 0 else result[-1]
        set_a[A[i] - 1] += 1
        if set_a[A[i] - 1] == 2:
            start_val += 1
        set_a[B[i] - 1] += 1
        if set_a[B[i] - 1] == 2:
            start_val += 1
        result.append(start_val)
        
    return result
