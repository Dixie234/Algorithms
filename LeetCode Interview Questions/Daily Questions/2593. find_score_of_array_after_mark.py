from heapq import heapify, heappop, heappush, heapreplace
from typing import List

#use min heap to keep track of minimum element order
#have stack to track indexes which have been marked (could also use a boolean array)
#Time complexity O(nlog(n)) - the emptying of the heap structure is nlog(n) time
#Space complexity O(n) - storing the heap and stack of all nums and indexes
def findScore(nums: List[int]) -> int:
    length = len(nums)
    nums_heap = [(num, i) for i, num in enumerate(nums)]
    heapify(nums_heap)
    marked = set()
    score = 0

    while nums_heap:
        num, index = heappop(nums_heap)
        if index not in marked:
            score += num
            marked.add(index)
            if index > 0:
                marked.add(index - 1)
            if index < length - 1:
                marked.add(index + 1)

    return score

#sliding window approach which moves in steps of 2 to account for marking of adjacent numbers
#once it finds an instance of an increasing number it works backwards through the window and adds the values to the score
#since all values in window are in decreasing order it will always add the next minimum value
#Time complexity O(n)
#Space complexity O(1)
def findScore(nums: List[int]) -> int:
    result = 0
    i = 0
    while i < len(nums):
        current_start = i
        while i + 1 < len(nums) and nums[i + 1] < nums[i]:
            i += 1
        current_index = i
        while current_index >= current_start:
            result += nums[current_index]
            current_index -= 2
        i += 2
    return result
        

#use monotonic decreasing stack to keep track of minimum values found
#add additional pop() to ensure that adjacent numbers are also removed
#Time complexity O(n)
#Space complexity O(n)
# def findScore(nums: List[int]) -> int:
#     stk = []
#     res = 0
#     for i in range(len(nums)):
#         #monotonic decreasing stack
#         if not stk or nums[i] < stk[-1]:
#             stk.append(nums[i])
#         else:
#             while stk:
#                 res += stk.pop()
#                 if stk:
#                     stk.pop()
#     while stk:
#         res += stk.pop()
#         if stk:
#             stk.pop()

#     return res

# #using start pointer to track numbers in descending order
# #space optimized version of stack implementation
# #Time complexity O(n)
# #Space complexity O(1)
# def findScore(nums: List[int]) -> int:
#     nums.append(float("inf"))
#     res = 0
#     start = -1
#     i = 1
#     while i < len(nums):
#         if nums[i] >= nums[i - 1]:
#             for j in range(i - 1, start, -2):
#                 res += nums[j]
#             start = i
#             i += 1
#         i += 1
#     return res

nums = [6,5,4,3,2,1]
result = findScore(nums)
print(result)