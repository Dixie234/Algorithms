from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    length = len(intervals)
    if length == 1:
        return intervals
    
    result = []
    prev = intervals[0]
    for i in range(1, length):
        first = intervals[i][0]
        second = intervals[i][1]
        if first <= prev[1]:
            prev[1] = second
        elif first <= prev[0]:
            prev[0] = first
        else:
            result.append(prev)
            prev = intervals[i]
    result.append(prev)
    
    return result

#intervals = [[1,3],[2,6],[8,10],[15,18]]
#[[1,3],[2,6],[8,10],[9,10],[10,11],[12,14]]
intervals = [[3,5],[4,5],[1,4],[4,5]]
result = merge(intervals)
print(result)