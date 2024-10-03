from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    val = None
    node_num = 0
    def dfs(root):
        nonlocal val, node_num
        if not root or val:
            return
        
        dfs(root.left)
        node_num += 1
        if node_num == k:
            val = root.val
        dfs(root.right)
    dfs(root)
    return val