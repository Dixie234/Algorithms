from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    length = len(intervals)
    if length == 1:
        return intervals
    
    result = []
    intervals.sort()
    i = 0
    while i < length:
        start = intervals[i]
        while i + 1 < length and is_overlap(start, intervals[i + 1]):
            start = merge_overlapping_intervals(start, intervals[i + 1])
            i += 1
        result.append(start)
        i += 1
    return result

def is_overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

def merge_overlapping_intervals(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

#[[1,3],[2,6],[8,10],[15,18]]
#[[1,3],[2,6],[8,10],[9,10],[10,11],[12,14]]
#[4, 1], [7, 4], [1, 2], [3, 8]]
intervals = [[3,5],[4,5],[1,4],[4,5],[7,7],[8,9]]
result = merge(intervals)
print(result)