from typing import List

def hourglassSum(arr:List[List[int]]) -> int:
    length = len(arr)
    offsets = [[0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
    result = -float("inf")
    for i in range(length):
        for j in range(length):
            cum_sum = arr[i][j]
            for add_i, add_j in offsets:
                if (i + add_i) >= length or (j + add_j) >= length:
                    cum_sum = -float("inf")
                    break
                else:
                    cum_sum += arr[i + add_i][j + add_j]
            result = max(result, cum_sum)
    return result

nums = """0 -4 -6 0 -7 -6
-1 -2 -6 -8 -3 -1
-8 -4 -2 -8 -8 -6
-3 -1 -2 -5 -7 -4
-3 -5 -3 -6 -6 -6
-3 -6 0 -8 -6 -7"""

rows = nums.split("\n")
cols = [row.split(" ") for row in rows]
arr = []
for i in range(len(cols)):
    arr.append([])
    for j in range(len(cols)):
        arr[i].append(int(cols[i][j]))

result = hourglassSum(arr)
print(result)


