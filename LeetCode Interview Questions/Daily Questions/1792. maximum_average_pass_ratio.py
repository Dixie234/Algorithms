from heapq import heapify, heappop, heappush
from typing import List

#wins 1st round (3/5) - (2/4)
#wins 2nd round (3/11) - (2/10)
#wins 3rd round (4/10) - (3/9)
#wins 4th round (4/6) - (3/5)
diff1 = (4/6) - (3/5)
diff2 = (5/11) - (4/10)
diff3 = (5/6) - (4/5)
diff4 = (4/12) - (3/11)

#creation of maximum heap which stores the largest difference increasing a given class by 1 extra student
#then, it iterates through the heap, reinserting the updated class ratio
def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:
    class_heap = [((((x / y) - (x + 1) / (y + 1))), [x, y]) for x, y in classes]
    heapify(class_heap)
    
    for i in range(extraStudents):
        curr_best = heappop(class_heap)
        old_ratio = curr_best[1]
        new_ratio = [x + 1 for x in old_ratio]
        new_val = ((new_ratio[0] / new_ratio[1]) - ((new_ratio[0] + 1) / (new_ratio[1] + 1)))
        heappush(class_heap, (new_val, new_ratio))

    return sum([y[0] / y[1] for x, y in class_heap]) / len(classes)

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2
result = maxAverageRatio(classes, extraStudents)
print(result)
