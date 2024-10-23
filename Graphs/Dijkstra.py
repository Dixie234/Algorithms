from heapq import heapify, heappop, heappush


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