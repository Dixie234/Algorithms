from collections import deque
import copy
from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, node):
        if node not in self.edges:
            self.edges.append(node)

def build_graph(edges:list[int, int]):
    graph:dict[int, Node] = {}
    for edge in edges:
        l = edge[0]
        r = edge[1]
        if l not in graph:
            graph[l] = Node(l)
        if r not in graph:
            graph[r] = Node(r)
        graph[l].add_edge(graph[r])
    return graph

#use Kahn's algorithm
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = build_graph(prerequisites)
    visited = set()

    def dfs(node:Node, visited_dfs:set):
        if node.value in visited_dfs:
            return False
        else:    
            visited_dfs.add(node.value)

        visited.add(node.value)

        for edge in node.edges:
            visited_copy = copy.deepcopy(visited_dfs)
            result = dfs(edge, visited_copy)
            if not result:
                return False

        return True

    for num, node in graph.items():
        if node.value not in visited:
            result = dfs(node, set())
            if not result:
                return False
            
    return True

# preq = [[1,0],[2,0],[0,2]]
# numCourses = 3
# prerequisites = [[1,2],[1,3],[1,4],[2,6],[3,5],[4,5]]
# numCourses = 7
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
numCourses = 5
result = canFinish(numCourses, prerequisites)
print(result)