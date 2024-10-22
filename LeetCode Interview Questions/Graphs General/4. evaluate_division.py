from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.adjacent_letters = {}

    def add_adjacent_letter(self, letter, weight):
        if letter not in self.adjacent_letters:
            self.adjacent_letters[letter] = weight

def build_graph(equations, values):
    graph = {}
    for i in range(len(values)):
        l, r = equations[i]
        weight = values[i]
        if l not in graph:
            graph[l] = Node(l)
        if r not in graph:
            graph[r] = Node(r)
        graph[l].add_adjacent_letter(r, weight)
        graph[r].add_adjacent_letter(l, 1.0 / weight)
    return graph

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = build_graph(equations, values)

    def dfs_search(node:Node, search_value:int, visited_letters:dict[int, bool]={}, path:float=1.0) -> Optional[Node]:
        if node.letter == search_value:
            return path
        
        visited_letters[node.letter] = True

        for letter, weight in node.adjacent_letters.items():
            curr_path = path * weight
            if letter not in visited_letters:
                if letter == search_value:
                    return curr_path
                
                search_path = dfs_search(graph[letter], search_value, visited_letters, curr_path)

                if search_path != -1:
                    return search_path
                
        return -1.0
    
    result = []
    for query in queries:
        if query[0] not in graph or query[1] not in graph:
            result.append(-1.0)
        else:
            result.append(dfs_search(graph[query[0]], query[1], {}))

    return result

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
result = calcEquation(equations, values, queries)


