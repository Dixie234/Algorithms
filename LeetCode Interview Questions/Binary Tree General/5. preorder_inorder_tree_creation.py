from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    pass

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]