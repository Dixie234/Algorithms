from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(postorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not postorder:
        return None
    
    inorder = { val: index for index, val in enumerate(inorder) }

    def build(start:int, end:int):
        if start > end:
            return None
        
        val = postorder.pop()
        mid = inorder[val]
        node = TreeNode(val)
        
        node.right = build(mid + 1, end)
        node.left = build(start, mid - 1)

        return node
            

    return build(0, len(inorder) - 1)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

result = buildTree(postorder, inorder)
print(result)