from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root: Optional[TreeNode]) -> int:
    min_val = float("inf")
    prev_node = None
    def dfs(root:Optional[TreeNode]):
        if not root:
            return
        
        nonlocal min_val, prev_node

        dfs(root.left)

        if prev_node:
            dist = root.val - prev_node.val
            min_val = min(min_val, dist)
        prev_node = root

        dfs(root.right)

    dfs(root)

    return min_val