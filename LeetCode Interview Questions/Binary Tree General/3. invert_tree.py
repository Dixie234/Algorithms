from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#using BFS (queue)
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    queue = deque([root])
    while queue:
        p = queue.popleft()
        if p:
            p.left, p.right = p.left, p.right
            queue.append(p.left)
            queue.append(p.right)

    return root

#Invert tree using DFS (recusion)
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)

    return root

def bfs(p: Optional[TreeNode]) -> bool:
    if not p:
        return None
    
    queue = deque([p])
    while queue:
        p = queue.popleft()
        if p:
            queue.append(p.left)
            queue.append(p.right)
    return p