from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.vals = [-1]
        self.dfs(root)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.vals[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.vals)
    
    def dfs(self, root:Optional[TreeNode]):
        if not root:
            return
        self.dfs(root.left)
        self.vals.append(root.val)
        self.dfs(root.right)