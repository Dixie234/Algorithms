from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    length = len(points)
    if length == 1:
        return 1
    
    points.sort(key=lambda x: x[1])
  
    result = 1
    end = points[0][1]
    for s, e in points:
        if s <= end:
            continue
        else:
            end = e
            result += 1
    return result

points = [[10,16],[2,8],[1,6],[7,12]]
points_sorted = [[1,6],[2,8],[7,12],[10,16]]
result = findMinArrowShots(points)
print(result)