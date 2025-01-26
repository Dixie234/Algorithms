from collections import deque
from typing import List

#Time limit exceeded
def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    nodes = len(graph)
    terminal_nodes = set([i for i in range(nodes) if not graph[i]])
    non_terminal_nodes = set()

    def dfs(root:int, visited:set):
        if root in visited:
            for node in visited:
                non_terminal_nodes.add(node)
        
        visited.add(root)
        adj_nodes = [adj_node for adj_node in graph[root] if adj_node not in terminal_nodes]
        if not adj_nodes:
            terminal_nodes.add(root)

        for node in adj_nodes:
            if node not in visited:
                dfs(node, visited)

        if all([adj_node in terminal_nodes for adj_node in adj_nodes]):
            terminal_nodes.add(root)

    for i in range(nodes):
        if i in terminal_nodes or i in non_terminal_nodes:
            continue
        dfs(i, set())

    return sorted(list(terminal_nodes))

#Graph given is only of the list of outgoing edges
#Once incoming edges and indegrees calculated, perform topological, starting with indegree = 0 nodes
#This uses a variation on Kahn's algorithm where instead of iterating through the outgoing edges for each node inside the queue
#It iterates through the incoming edges, and if the indegree == 0 then it must be safe
#Since all nodes which started in the queue were Terminal Nodes.
#Kahn's algorithm avoids cycles, which is what we want since cycles are unsafe nodes.
#Time Complexity O(m + n) - Kahn's algorithm takes O(m + n) time, reversing the graph takes O(m + n) as well but simplifies to O(m + n)
#Space Complexity O(m + n) - Adjaency array takes up m space, safe array takes up n space. Therefore O(m + n)
def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    nodes = len(graph)
    #Create adjacency graph of all incoming edges
    indegrees = [0] * nodes
    reverse_graph = [[] for _ in range(nodes)]
    for i in range(nodes):
        for node in graph[i]:
            reverse_graph[node].append(i)
            indegrees[i] += 1

    #Create a queue of all nodes with 0 incoming edges
    queue = deque([i for i in range(nodes) if indegrees[i] == 0])

    #Create array to track all nodes which are safe
    safe = [False] * nodes

    while queue:
        curr = queue.popleft()
        safe[curr] = True

        for node in reverse_graph[curr]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                queue.append(node)

    return [i for i in range(nodes) if safe[i]]

# [[],[0,2,3,4],[3],[4],[]]
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
result = eventualSafeNodes(graph)
print(result)
    
