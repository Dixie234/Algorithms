from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    length = len(intervals)
    if length == 0:
        return [newInterval]
    
    intervals.append(newInterval)
    return merge(intervals)

def is_overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

def merge_overlapping_intervals(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

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

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

result = insert(intervals, newInterval)
print(result)
