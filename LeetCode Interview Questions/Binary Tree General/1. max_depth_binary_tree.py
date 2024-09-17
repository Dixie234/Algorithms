from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    ldepth = maxDepth(root.left)
    rdepth = maxDepth(root.right)

    return max(ldepth, rdepth) + 1