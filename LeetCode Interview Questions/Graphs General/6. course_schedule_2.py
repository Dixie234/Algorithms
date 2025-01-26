from collections import deque
from typing import List

#As in course_schedule.py, this requires a topological sort of the graph.
#Rather than just seeing if the graph contains cycles, instead you need to return the graphs order.
#Kahn's algorithm does this for you, however, in order to be in the correct order for this problem
#It need to be reversed to show which classes to start with.
#Time Complexity O(m + n) - Kahn's algorithm visits all nodes and edges in worst case.
#Space Complexity O(m + n) - Adjaency array is of length m and indegrees is of length n.
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    indegree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    for edge in prerequisites:
        adj[edge[0]].append(edge[1])
        indegree[edge[1]] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr)
        for neighbour in adj[curr]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
                
    if len(result) != numCourses:
        return []
    else:
        return list(reversed(result))