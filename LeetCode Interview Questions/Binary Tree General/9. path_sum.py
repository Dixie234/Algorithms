from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    makes_sum = False

    def track_sum(root: Optional[TreeNode], total=0):
        if not root:
            return
        
        total += root.val
        if not root.left and not root.right:
            if total == targetSum:
                nonlocal makes_sum
                makes_sum = True
        
        track_sum(root.left, total)
        track_sum(root.right, total)

    track_sum(root)

    return makes_sum

#minus current value from result to whittle down the result to desired value
#by the time you get to the leaf node, you just need to compare it's val and the sum
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    
    if not root.left and not root.right:
        return targetSum == root.val
    
    left_sum = self.hasPathSum(root.left, targetSum - root.val)
    right_sum = self.hasPathSum(root.right, targetSum - root.val)
    
    return left_sum or right_sum

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(4, None, node1)
node5 = TreeNode(13)
node6 = TreeNode(11, node3, node2)
node7 = TreeNode(8, node5, node4)
node8 = TreeNode(4, node6)
node9 = TreeNode(5, node8, node7)

result = hasPathSum(node9, 22)
print(result)