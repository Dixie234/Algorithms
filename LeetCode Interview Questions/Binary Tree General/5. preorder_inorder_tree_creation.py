from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None
    
    preorder = deque(preorder)
    inorder = { val: index for index, val in enumerate(inorder) }

    def build(start:int, end:int):
        if start > end:
            return None
        
        val = preorder.popleft()
        mid = inorder[val]
        node = TreeNode(val)

        node.left = build(start, mid - 1)
        node.right = build(mid + 1, end)

        return node
            

    return build(0, len(inorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

result = buildTree(preorder, inorder)
print(result)