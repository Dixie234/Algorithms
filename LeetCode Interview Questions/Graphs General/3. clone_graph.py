from collections import deque
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def add_adjacent_node(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

def cloneGraph(node: Optional['Node']) -> Optional['Node']:
    if not node:
        return node
    
    visited = {
        node.val: Node(node.val)
    }
 
    queue = deque([node])
    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = Node(neighbor.val)
                queue.append(neighbor)
            visited[curr.val].neighbors.append(visited[neighbor.val])
    return visited[node.val]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.add_adjacent_node(node2)
node1.add_adjacent_node(node4)

node2.add_adjacent_node(node1)
node2.add_adjacent_node(node3)

node3.add_adjacent_node(node2)
node3.add_adjacent_node(node4)

node4.add_adjacent_node(node1)
node4.add_adjacent_node(node3)

result = cloneGraph(node1)
print(result)