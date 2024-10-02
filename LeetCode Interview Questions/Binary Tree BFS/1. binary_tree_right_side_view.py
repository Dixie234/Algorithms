from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> List[int]:    
    queue = deque([root])
    right_view = []
    while queue:
        length = len(queue)
        for i in range(length):
            node = queue.popleft()
            if i == (length - 1):
                right_view.append(node.val)
            if node.left: 
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
    return right_view

node9 = TreeNode(0)
node10 = TreeNode(8)
node1 = TreeNode(1, node9, node10)
node4 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(4)
node5 = TreeNode(2, node7, node8)
node2 = TreeNode(5, node4, node5)
node3 = TreeNode(3, node2, node1)

result = rightSideView(node3)
print(result)


