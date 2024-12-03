from typing import List


def countSquares(matrix: List[List[int]]) -> int:
    total = sum([sum(nums) for nums in  matrix])
    if total == 0:
        return 0
    
    height = len(matrix)
    width = len(matrix[0])
    max_square = min(height, width) 

    return 1