from collections import Counter
from typing import List


def maxPoints(points: List[List[int]]) -> int:
    length = len(points)
    if length == 1:
        return 1
    
    x_count = Counter([point[0] for point in points])
    y_count = Counter([point[1] for point in points])

    lines = set()
    for i in range(length - 1):
        for j in range(1 + i, length):
            line = define_line(points[i], points[j])
            lines.add(line)
    counts = Counter()
    for key in lines:
        for point in points:
            epsilon = 1e-9
            if abs(point[1] - ((key[0] * point[0]) + key[1])) <= epsilon:
                counts[key] += 1
    return max(counts.most_common(1)[0][1], x_count.most_common(1)[0][1], y_count.most_common(1)[0][1])

def define_line(point_a:list[int], point_b:list[int]) -> tuple[int, int]:
    x_diff, y_diff = point_a[0] - point_b[0], point_a[1] - point_b[1]
    m = y_diff / x_diff if y_diff != 0 and x_diff != 0 else 0
    c = point_a[1] - (m * point_a[0])
    return (m, c)

point_b = [3,2]
point_a = [5,7]
#points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
#points = [[4,5],[4,-1],[4,0]]
points = [[-6,-1],[3,1],[12,3]]
result = maxPoints(points)
print(result)