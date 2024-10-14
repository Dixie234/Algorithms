from collections import deque
from heapq import heapify, heappop, heappush
from typing import List, Optional

def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)  # Undirected

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

# Create a graph with 4 vertices and no edges
V = 4
adj = [[] for _ in range(V)]

# Now add edges one by one
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 2, 3)

print("Adjacency List Representation:")
display_adj_list(adj)


class Vertex:
    def __init__(self, value:int):
        self.value = value
        #using adjacency array
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex:"Vertex"):
        if vertex not in self.adjacent_vertices:
            self.adjacent_vertices.append(vertex)

def dfs(vertex:Vertex, visited_vertices:dict[int, bool]={}):
    visited_vertices[vertex.value] = True

    print(vertex.value)

    for adj_vertex in vertex.adjacent_vertices:
        if adj_vertex.value not in visited_vertices:
            dfs(adj_vertex, visited_vertices)

def dfs_search(vertex:Vertex, search_value:int, visited_vertices:dict[int, bool]={}) -> Optional[Vertex]:
    if vertex.value == search_value:
        return vertex
    
    visited_vertices[vertex.value] = True

    for adj_vertex in vertex.adjacent_vertices:
        if adj_vertex.value not in visited_vertices:
            if adj_vertex.value == search_value:
                return adj_vertex
            
            search_vertex = dfs_search(adj_vertex, search_value, visited_vertices)

            if search_vertex:
                return search_vertex
            
    return None

def bfs(vertex:Vertex):
    queue = deque([vertex])

    visited_verticies = {
        vertex.value: True
    }

    while queue:
        curr = queue.popleft()
        print(curr.value)
        for adj_vertex in curr.adjacent_vertices:
            if adj_vertex.value not in visited_verticies:
                visited_verticies[adj_vertex.value] = True
                queue.append(adj_vertex)

class WeightedGraphVertex:
    def __init__(self, value:int):
        self.value = value
        self.adjacent_vertices = {}

    def add_adjacent_vertex(self, vertex:"WeightedGraphVertex", weight:int):
        self.adjacent_vertices[vertex] = weight

def dijkstra(start:WeightedGraphVertex, end:WeightedGraphVertex):
    shortest_paths = {}
    previous_vertex = {}

    unvisited_vertices = heapify([])
    visited_verticies = {}

    shortest_paths[start.value] = 0
    curr = start
    while curr:
        visited_verticies[curr.value] = True

        for adj_vertex, price in curr.adjacent_vertices.items():
            if adj_vertex.value not in visited_verticies:
                heappush(unvisited_vertices, adj_vertex)
                
            curr_total = shortest_paths[curr.value] + price

            if adj_vertex.value not in shortest_paths or curr_total < shortest_paths[adj_vertex.value]:
                shortest_paths[adj_vertex.value] = curr_total
                previous_vertex[adj_vertex.value] = curr.value
    
        curr = heappop(unvisited_vertices)

    shortest_path = []
    curr_val = end.value
    while curr_val != start.value:
        shortest_path.append(curr_val)
        curr_val = previous_vertex[curr_val]

    shortest_path.append(start.value)
    shortest_path.reverse()
    return shortest_path

