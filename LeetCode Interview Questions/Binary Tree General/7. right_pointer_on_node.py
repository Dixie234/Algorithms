from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    levels:dict[int, Node] = {}

    def setNext(root: Optional[Node], depth=0) -> None:
        if not root:
            return
        
        setNext(root.left, depth + 1) 
        setNext(root.right, depth + 1)

        if depth in levels:
            levels[depth].next = root        
        levels[depth] = root
    
    setNext(root)

    return root

node1 = Node(1, None, None)
node2 = Node(2, None, None)
node3 = Node(3, None, None)
node4 = Node(4, None, None)
node5 = Node(5, node2, node1)
node6 = Node(6, node4, node3)
node7 = Node(7, node6, node5)

result = connect_perfect_tree(node7)
    


