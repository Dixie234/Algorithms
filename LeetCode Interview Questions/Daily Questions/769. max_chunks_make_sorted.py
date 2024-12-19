from typing import List


def maxChunksToSorted(arr: List[int]) -> int:
    result = 0
    max_val = 0
    for i in range(len(arr)):
        max_val = max(max_val, arr[i])
        if max_val == i:
            result += 1
    return result

arr = [1,0,2,3,4]
result = maxChunksToSorted(arr)
print(result)

# def increasing_monotonic_queue(arr):
#     n = len(arr)
#     q = deque()
#     for i in range(n):
#         # If recently added element is
#         # larger than current element
#         while q and q[-1] > arr[i]:
#             q.pop()
#         q.append(arr[i])
#     return q