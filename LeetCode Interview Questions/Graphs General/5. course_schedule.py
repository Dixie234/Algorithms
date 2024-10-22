from collections import deque
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

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = build_graph(prerequisites)
    visited = set()

    def bfs(node:Node):
        queue = deque([node])
        visited_bfs = set([node])
        visited.add(node)

        while queue:
            curr = queue.popleft()
            for edge in curr.edges:
                if edge.value == node.value:
                    return False
                if edge not in visited:
                    visited.add(edge)
                if edge not in visited_bfs:
                    queue.append(edge)
                    visited_bfs.add(edge)
        return True
    
    for num, node in graph.items():
        if node not in visited:
            result = bfs(node)
            if not result:
                return False
            
    return True

preq = [[1,0],[2,0],[0,2]]
numCourses = 3
result = canFinish(numCourses, preq)
print(result)