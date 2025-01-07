from typing import List

#Time Complexity O(n^2) - In worst case all boxes have a ball and therefore for every box iteration iterates through the entire boxes_set
#Space Complexity O(n) - Stores the set of size n and the result of size n, making O(2n), which simplifies to O(n)
def minOperations(boxes: str) -> List[int]:
    boxes_set = set([i for i, box in enumerate(boxes) if box == "1"])
    result = []
    for i in range(len(boxes)):
        total_moves = 0
        for box_index in boxes_set:
            total_moves += abs(i - box_index)
        result.append(total_moves)
    return result