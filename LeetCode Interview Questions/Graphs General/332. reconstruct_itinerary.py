from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List

#Use variation of Heirzolers with the addition of a min heap instead of a list for the edges
#This allows for faster derivations of the lowest lexical node
def findItinerary(tickets: List[List[str]]) -> List[str]:
    adj_matrix = defaultdict(list)
    for start, end in tickets:
        if start not in adj_matrix:
            adj_matrix[start] = [end]
            heapify(adj_matrix[start])
        else:
            heappush(adj_matrix[start], end)

    result = []
    stack = ["JFK"]
    while stack:
        node = stack[-1]
        if adj_matrix[node]:
            next = heappop(adj_matrix[node])
            stack.append(next)
        else:
            result.append(node)
            stack.pop()
    return result[::-1]


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
result = findItinerary(tickets)
print(result)