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

def inorder_dfs(root:Optional[TreeNode]) -> None:
    if not root:
        return
    
    inorder_dfs(root.left)

    print(root.val, end=" ")

    inorder_dfs(root.right)

def preorder_dfs(root:Optional[TreeNode]) -> None:
    if not root:
        return
    
    print(root.val, end=" ")

    preorder_dfs(root.left)
    preorder_dfs(root.right)

def postorder_dfs(root:Optional[TreeNode]) -> None:
    if not root:
        return
    
    postorder_dfs(root.left)
    postorder_dfs(root.right)
    
    print(root.val, end=" ")

# Preorder traversal without  
# recursion and without stack 
def MorrisTraversal(root): 
    curr = root 
  
    while curr: 
        # If left child is null, print the 
        # current node data. And, update  
        # the current pointer to right child. 
        if curr.left is None: 
            print(curr.val, end= " ") 
            curr = curr.right 
  
        else: 
            # Find the inorder predecessor 
            prev = curr.left 
  
            while prev.right is not None and prev.right is not curr: 
                prev = prev.right 
  
            # If the right child of inorder 
            # predecessor already points to 
            # the current node, update the  
            # current with it's right child 
            if prev.right is curr: 
                prev.right = None
                curr = curr.right 
                  
            # else If right child doesn't point 
            # to the current node, then print this 
            # node's data and update the right child 
            # pointer with the current node and update 
            # the current with it's left child 
            else: 
                print (curr.val, end=" ") 
                prev.right = curr  
                curr = curr.left 

# Driver program to test  
root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
  
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
  
root.right.left= TreeNode(6) 
root.right.right = TreeNode(7) 
  
root.left.left.left = TreeNode(8) 
root.left.left.right = TreeNode(9) 
  
root.left.right.left = TreeNode(10) 
root.left.right.right = TreeNode(11) 
  
  
MorrisTraversal(root) 
print("\n") 
preorder_dfs(root) 
