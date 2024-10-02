from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    left_depth = get_depth(root.left)
    right_depth = get_depth(root.right)
    if left_depth == right_depth:
        result = pow(2, left_depth) + countNodes(root.right)
    else:
        result = pow(2, right_depth) + countNodes(root.left)

    return result


def get_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + get_depth(root.left)
