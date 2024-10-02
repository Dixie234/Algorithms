from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#dfs plus dict
def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    level_count:dict[int, int] = {}
    level_total:dict[int, int] = {}

    def setNext(root: Optional[TreeNode], depth=0) -> None:
        nonlocal level_count, level_total
        if not root:
            return
        
        if depth in level_count:
            level_count[depth] += 1
        else:
            level_count[depth] = 1

        if depth in level_total:
            level_total[depth] += root.val
        else:
            level_total[depth] = root.val

        setNext(root.left, depth + 1) 
        setNext(root.right, depth + 1)
    
    setNext(root)
    result = []
    for key, value in level_count.items():
        result.append(level_total[key] / value)

    return result

#bfs
def averageOfLevels(root: TreeNode) -> List[float]:
    q, ans = [root], []
    while len(q):
        qlen, row = len(q), 0
        for i in range(qlen):
            curr = q.pop(0)
            row += curr.val
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        ans.append(row/qlen)
    return ans

node9 = TreeNode(0)
node10 = TreeNode(8)
node1 = TreeNode(1, node9, node10)

node4 = TreeNode(6)

node7 = TreeNode(7)
node8 = TreeNode(4)

node5 = TreeNode(2, node7, node8)

node2 = TreeNode(5, node4, node5)
node3 = TreeNode(3, node2, node1)
result = averageOfLevels(node3)
print(result)