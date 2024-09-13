from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Using depth-first approach
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    if p is not None and q is not None:
        return ((p.val == q.val) and
                isSameTree(p.left, q.left) and
                isSameTree(p.right, q.right))

    return False

#Using breadth-first approach
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    
    pairs = deque([(p, q)])
    while pairs:
        p, q = pairs.popleft()
        if not isSame(p, q):
            return False            
        if p:
            pairs.append((p.left, q.left))
            pairs.append((p.right, q.right))
    return True

def isSame(node1:Optional[TreeNode], node2:Optional[TreeNode]):
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.val != node2.val:
        return False
    return True

# Creating the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
#print(result)