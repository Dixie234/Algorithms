from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    
    queue = deque([root])
    result = []
    while queue:
        level_list = []
        for i in range(len(queue)):
            node = queue.popleft()
            level_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_list)
    return result

    
