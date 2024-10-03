from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    level = 1
    while queue:
        level_list = deque()
        for i in range(len(queue)):
            node = queue.popleft()
            if level % 2 == 0:
                level_list.appendleft(node.val)
            else:
                level_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_list)
        level += 1
    return result
                
