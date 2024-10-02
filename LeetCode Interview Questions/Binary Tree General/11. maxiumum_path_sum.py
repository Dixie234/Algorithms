from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: Optional[TreeNode]) -> int:
    max_val = float("-inf")
    def dfs(root: Optional[TreeNode]) -> int:
        nonlocal max_val
        if not root:
            return 0
        
        left = max(dfs(root.left), 0)
        right = max(dfs(root.right), 0)

        curr_max = left + right + root.val
        max_val = max(curr_max, max_val)

        return root.val + max(left, right)
    
    dfs(root)
    return max_val
