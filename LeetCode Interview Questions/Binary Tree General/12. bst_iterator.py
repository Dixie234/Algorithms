from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def next(self) -> int:
        return 0
        

    def hasNext(self) -> bool:
        return False