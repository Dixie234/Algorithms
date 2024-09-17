from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#breadth-first approach
def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root.left and not root.right:
        return True
    
    p = root.left
    q = root.right
    pairs = deque([(p, q)])
    while pairs:
        p, q = pairs.popleft()
        if not isSame(p, q):
            return False            
        if p:
            pairs.append((p.left, q.right))
            pairs.append((p.right, q.left))
    return True        

def isSame(node1:Optional[TreeNode], node2:Optional[TreeNode]):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.val != node2.val:
        return False
    return True

#depth-first approach (recursion)
def isSymmetric(root: Optional[TreeNode]) -> bool:
    return isSameTree(root.left, root.right)

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    if p is not None and q is not None:
        return ((p.val == q.val) and
                isSameTree(p.left, q.right) and
                isSameTree(p.right, q.left))

    return False  
