from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: Optional[TreeNode]) -> int:
    def get_sums(root: Optional[TreeNode], total=0):
        if not root:
            return 0
        
        total = (total * 10) + root.val
        if not root.left and not root.right:
            return total
        return get_sums(root.left, total) + get_sums(root.right, total)

    return get_sums(root)
