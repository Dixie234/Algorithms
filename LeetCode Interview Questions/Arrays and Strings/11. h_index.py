from typing import List

citations = [1]

def hIndex(citations: List[int]) -> int:
    citations.sort(reverse=True)
    h_index = 0
    for i, num in enumerate(citations):
        if i + 1 > num:
            break
        h_index += 1
    return h_index


result = hIndex(citations)
print(result)
