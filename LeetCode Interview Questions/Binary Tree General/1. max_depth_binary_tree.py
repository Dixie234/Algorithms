from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    ldepth = maxDepth(root.left)
    rdepth = maxDepth(root.right)

    return max(ldepth, rdepth) + 1

def currentDepth(root: Optional[TreeNode], depth=0) -> None:
    if not root:
        return
    
    currentDepth(root.left, depth + 1)    
    print(f'node:{root.val} depth:{depth}')
    currentDepth(root.right, depth + 1)

node1 = TreeNode(1, None, None)
node2 = TreeNode(2, None, None)
node3 = TreeNode(3, None, None)
node4 = TreeNode(4, None, None)
node5 = TreeNode(5, node2, node1)
node6 = TreeNode(6, node4, node3)
node7 = TreeNode(7, node6, node5)




