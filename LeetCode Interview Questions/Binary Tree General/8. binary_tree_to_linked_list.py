from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: Optional[TreeNode]) -> None:
    if not root:
        return
    
    ordered_nodes:List[TreeNode] = []
    
    def add_nodes(root: Optional[TreeNode]):
        if not root:
            return
        
        ordered_nodes.append(root)
        
        add_nodes(root.left)
        add_nodes(root.right)
    
    add_nodes(root)

    for i in range(len(ordered_nodes) - 1):
        ordered_nodes[i].left = None
        ordered_nodes[i].right = ordered_nodes[i + 1]

