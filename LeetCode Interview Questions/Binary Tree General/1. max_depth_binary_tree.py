from typing import Optional


def binary_search(x:int, arr:list):
    low = 0
    high = len(arr) -1
    med = 0
    while high >= low:
        med = (high + low) // 2
        if x > arr[med]:
            low = med + 1
        elif x < arr[med]:
            high = med - 1
        else:
            return med
    return -1

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