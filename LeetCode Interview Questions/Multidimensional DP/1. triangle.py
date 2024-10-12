from typing import List


#[[2],
# [3,4],
# [6,5,7],
# [4,1,8,3]]
def minimumTotal(triangle: List[List[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            prev_minus_one = float("inf")
            if j != 0:
                prev_minus_one = triangle[i - 1][j - 1]
            prev = float("inf")
            if j != len(triangle[i]) - 1:
                prev = triangle[i - 1][j]
            triangle[i][j] = triangle[i][j] + min(prev, prev_minus_one)
    return min(triangle[-1])

#alternative approach working from the bottom up
def minimumTotal(triangle):
    n = len(triangle)
    # Start from the second last row and move upwards
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            min_sum = min(triangle[i + 1][j], triangle[i + 1][j + 1])
            current_val = triangle[i][j]
            triangle[i][j] = current_val + min_sum
    return triangle[0][0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
result = minimumTotal(triangle)
print(result)

