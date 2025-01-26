from collections import deque
import copy
from typing import List

#use Kahn's algorithm to iterate throught the graph
#This performs a topological sort of the graph and excludes any cycles that it finds since cycles cannot be sorted.
#In this problem we need to see if all courses are completeable, therefore there must be 0 cycles
#If this is the case then the number of nodes visited must == numCourses
#Time Complexity O(m + n) - Visits all nodes and edges in worst case.
#Space Complexity O(m + n) - Adjaency array is of length m and indegrees is of length n.
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    indegree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    for edge in prerequisites:
        indegree[edge[1]] += 1
        adj[edge[0]].append(edge[1])

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    result = 0
    while queue:
        curr = queue.popleft()
        result += 1
        for neighbour in prerequisites[curr]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    return result == numCourses


# preq = [[1,0],[2,0],[0,2]]
# numCourses = 3
# prerequisites = [[1,2],[1,3],[1,4],[2,6],[3,5],[4,5]]
# numCourses = 7
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
numCourses = 5
result = canFinish(numCourses, prerequisites)
print(result)