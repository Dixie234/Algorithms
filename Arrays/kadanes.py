from typing import List

#Kadane's is an algorithm for calculating the maximum sum of a subarray within an array
#Calculates the cumulative sum of the array in one pass, 
#if the current element is larger than the sum of the previous elements, then it will reset the subarray to that element
#Time complexity O(n)
#Space complexity O(1)
def kadanes(arr:List[int]) -> int:
    result = arr[0]
    max_end = arr[0]
    for i in range(1, len(arr)):
        max_end = max(max_end + arr[i], arr[i])
        result = max(result, max_end)
    return abs(result)
