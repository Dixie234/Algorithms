from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#Breadth-first search approach which on even levels also stores the nodes values in vals
#Then, because vals and queue are inserted in opposite order to one another 
#it's just a simple case of updating the queue values with the same index in vals
#Time Complexity O(n) - Breadth-first search is O(n)
#Space complexity O(n) - vals and queue both store the same number of elements as a level in the tree, which tends towards O(n)
def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root.left:
        return root
    
    queue = deque([root])
    depth = 0
    while queue:
        if depth % 2 == 0:
            vals = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    vals.appendleft(node.left.val)
                if node.right:
                    queue.append(node.right)
                    vals.appendleft(node.right.val)

            for i in range(len(queue)):
                queue[i].val = vals[i]
        else:        
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        depth += 1
    return root

#Depth-first search approach using a search of both left and right nodes simultaniously
#Becuase it's a perfect binary tree, there will always be a compare value on either branch of the tree
#In order to reverse the list correctly, opposite left right children are passed down recursively
#Time Complexity O(n) - Depth-first search takes O(n) time
#Space Complexity O(log(n)) - This is determined by the recursion depth of the DFS, which for a perfect binary tree is O(log(n))
def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root.left:
        return root
    def dfs(left, right, depth=0):
        if not left:
            return
        
        if depth % 2 == 0:
            left.val, right.val = right.val, left.val
        
        dfs(left.left, right.right, depth + 1)
        dfs(left.right, right.left, depth + 1)
    dfs(root.left, root.right)
    return root
            