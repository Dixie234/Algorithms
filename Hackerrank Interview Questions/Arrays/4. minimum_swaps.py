from typing import List


def minimumSwaps(arr:List[int]):
    result = 0
    arr_map = { k:i for i, k in enumerate(arr) }
    for i in range(len(arr)):
        if arr[i] != (i + 1):
            correct_index = arr_map[i + 1]
            arr_map[arr[i]] = correct_index
            arr_map[i + 1] = i
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
            result += 1
    return result

arr = [4,3,1,2]
result = minimumSwaps(arr)
print(result)


    