from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    is_valid = True
    prev_node = None
    def dfs(root):
        nonlocal is_valid, prev_node
        
        if not root or not is_valid:
            return
        
        dfs(root.left)

        if prev_node:
            if prev_node.val >= root.val:
                is_valid = False
        prev_node = root

        dfs(root.right)
    dfs(root)
    return is_valid
