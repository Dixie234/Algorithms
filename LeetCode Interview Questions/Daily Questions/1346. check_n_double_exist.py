from typing import Counter, List


def checkIfExist(arr: List[int]) -> bool:
    arr_dict = Counter(arr)
    for val in arr:
        if val * 2 in arr_dict and val != 0:
            return True
        elif val == 0 and arr_dict[val] > 1:
            return True
    return False     
    