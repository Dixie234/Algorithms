from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root:Optional[TreeNode]) -> None:
    if not root:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs(root:Optional[TreeNode]) -> None:
    if not root:
        return
    
    print(root.val, end=" ")

    dfs(root.left)
    dfs(root.right)

def inorder_dfs(root:Optional[TreeNode]) -> None:
    if not root:
        return
    
    dfs(root.left)

    print(root.val, end=" ")

    dfs(root.right)

def preorder_dfs(root:Optional[TreeNode]) -> None:
    if not root:
        return
    
    print(root.val, end=" ")

    dfs(root.left)
    dfs(root.right)

def postorder_dfs(root:Optional[TreeNode]) -> None:
    if not root:
        return
    
    dfs(root.left)
    dfs(root.right)
    
    print(root.val, end=" ")
